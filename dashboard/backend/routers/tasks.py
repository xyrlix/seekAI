"""
任务 API 路由
"""

from fastapi import APIRouter, Query
from typing import Optional
from schemas import Task, TaskList

router = APIRouter(prefix="/api/tasks", tags=["任务"])


@router.get("", response_model=TaskList)
async def get_tasks(phase: Optional[int] = Query(None)):
    """获取任务列表"""
    from database import get_tasks

    tasks = get_tasks(user_id=1, phase=phase)
    completed = sum(1 for t in tasks if t["status"] == "completed")

    return TaskList(
        tasks=[Task(**t) for t in tasks],
        total=len(tasks),
        completed=completed
    )


@router.get("/{task_id}", response_model=Task)
async def get_task(task_id: int):
    """获取单个任务详情"""
    from database import get_tasks

    tasks = get_tasks(user_id=1)
    for t in tasks:
        if t["id"] == task_id:
            return Task(**t)

    return Task(id=task_id, phase=0, week=0, name="未知任务")
