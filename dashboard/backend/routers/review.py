"""
评分 API 路由
"""

from fastapi import APIRouter, Depends
from dashboard.backend.schemas import ReviewRequest, ReviewResponse
from dashboard.backend.auth.dependencies import get_current_user

router = APIRouter(prefix="/api/review", tags=["评分"])


@router.post("", response_model=ReviewResponse)
async def submit_review(review: ReviewRequest, current_user: dict = Depends(get_current_user)):
    """提交代码评分"""
    from dashboard.backend.database import update_task_score

    # 计算总分
    total = (
        review.correctness +
        review.conventions +
        review.performance +
        review.readability
    ) // 4

    # 更新数据库
    update_task_score(
        task_id=review.task_id,
        score=total,
        review_data={
            "correctness": review.correctness,
            "conventions": review.conventions,
            "performance": review.performance,
            "readability": review.readability
        }
    )

    return ReviewResponse(
        total=total,
        passed=total >= 7  # Phase 1 通过标准：>=7/10
    )
