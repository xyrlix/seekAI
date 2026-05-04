"""
进度 API 路由
"""

from fastapi import APIRouter, Depends
from dashboard.backend.schemas import ProgressResponse
from dashboard.backend.auth.dependencies import get_current_user

router = APIRouter(prefix="/api/progress", tags=["进度"])


@router.get("", response_model=ProgressResponse)
async def get_progress(current_user: dict = Depends(get_current_user)):
    """获取用户学习进度"""
    from dashboard.backend.database import get_user_progress

    progress = get_user_progress(user_id=current_user["user_id"])

    return ProgressResponse(
        total=progress["total"],
        completed=progress["completed"],
        avg_score=progress["avg_score"],
        phases=progress["phases"]
    )