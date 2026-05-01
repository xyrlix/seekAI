"""
seekAI Dashboard 后端 API
FastAPI + SQLite
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import progress, tasks, review

app = FastAPI(
    title="seekAI Dashboard API",
    description="AI 开发训练系统进度可视化 API",
    version="1.0.0"
)

# CORS 配置，允许前端访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(progress.router)
app.include_router(tasks.router)
app.include_router(review.router)


@app.get("/")
async def root():
    """根路径"""
    return {"message": "seekAI Dashboard API", "version": "1.0.0"}


@app.get("/api/stats")
async def get_stats():
    """获取统计数据"""
    from database import get_user_progress, get_tasks

    progress = get_user_progress(user_id=1)
    tasks = get_tasks(user_id=1)
    completed = [t for t in tasks if t["status"] == "completed"]

    return {
        "total_tasks": progress["total"],
        "completed_tasks": progress["completed"],
        "total_score": progress["avg_score"],
        "current_streak": len(completed),  # 简化：完成任务数作为连续天数
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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
