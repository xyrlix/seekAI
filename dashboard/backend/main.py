"""
seekAI Dashboard 后端 API
FastAPI + SQLite
"""

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from dashboard.backend.routers.progress import router as progress_router
from dashboard.backend.routers.tasks import router as tasks_router
from dashboard.backend.routers.review import router as review_router
from dashboard.backend.routers.abilities import router as abilities_router
from dashboard.backend.auth import router as auth_router, get_current_user

app = FastAPI(
    title="seekAI Dashboard API",
    description="AI 开发训练系统进度可视化 API",
    version="1.0.0"
)

# CORS 配置，允许前端访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(auth_router)
app.include_router(progress_router)
app.include_router(tasks_router)
app.include_router(review_router)
app.include_router(abilities_router)


@app.get("/")
async def root():
    """根路径"""
    return {"message": "seekAI Dashboard API", "version": "1.0.0"}


@app.get("/api/stats")
async def get_stats(current_user: dict = Depends(get_current_user)):
    """获取统计数据"""
    from dashboard.backend.database import get_user_progress, get_tasks, update_abilities_by_progress

    user_id = current_user["user_id"]
    update_abilities_by_progress(user_id=user_id)
    progress = get_user_progress(user_id=user_id)
    tasks = get_tasks(user_id=user_id)
    completed = [t for t in tasks if t["status"] == "completed"]

    return {
        "total_tasks": progress["total"],
        "completed_tasks": progress["completed"],
        "total_score": progress["avg_score"],
        "current_streak": len(completed),
        "achievements_count": 0
    }


@app.get("/api/achievements")
async def get_achievements():
    """获取成就列表"""
    # 预定义成就
    achievements = [
        {
            "id": 1,
            "name": "初学者",
            "description": "完成第一个任务",
            "icon": "🌱",
            "unlocked_at": None
        },
        {
            "id": 2,
            "name": "Python 入门",
            "description": "完成 Phase 1 Week 1-2",
            "icon": "🐍",
            "unlocked_at": None
        },
        {
            "id": 3,
            "name": "函数掌握",
            "description": "完成 Week 3-4 函数模块",
            "icon": "⚡",
            "unlocked_at": None
        },
        {
            "id": 4,
            "name": "数据分析师",
            "description": "完成 numpy/pandas 任务",
            "icon": "📊",
            "unlocked_at": None
        },
        {
            "id": 5,
            "name": "代码审查员",
            "description": "获得 10 次代码审查",
            "icon": "🔍",
            "unlocked_at": None
        }
    ]
    return achievements


@app.post("/api/execute")
async def execute_code(request: dict):
    """在线执行 Python 代码 - 已弃用，请使用 Pyodide 浏览器内执行"""
    import sys
    from io import StringIO

    code = request.get("code", "")
    if not code:
        return {"output": "No code provided", "error": None}

    # 重定向 stdout 以捕获 print 输出
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    try:
        # 使用 exec 执行代码（限制作用域）
        exec_globals = {"__builtins__": __builtins__}
        exec(code, exec_globals)
        output = sys.stdout.getvalue()
        return {"output": output, "error": None}
    except Exception as e:
        output = sys.stdout.getvalue()
        return {"output": output, "error": str(e)}
    finally:
        sys.stdout = old_stdout


@app.post("/api/execution/results")
async def save_execution_result(request: dict):
    """存储代码执行结果（供进度追踪使用，代码执行已移至浏览器 Pyodide）"""
    from dashboard.backend.database import get_connection

    data = request
    user_id = data.get("user_id", 1)
    task_id = data.get("task_id")
    code = data.get("code", "")
    output_result = data.get("output", "")
    error = data.get("error")
    passed = error is None

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO reviews (task_id, correctness, conventions, performance, readability, total, created_at)
        VALUES (?, ?, ?, ?, ?, ?, datetime('now'))
    """, (task_id, 8 if passed else 5, 8, 8, 8, 8 if passed else 5))

    conn.commit()
    conn.close()

    return {"saved": True, "passed": passed}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
