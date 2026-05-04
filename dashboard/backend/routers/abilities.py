"""
能力 API 路由
"""

from fastapi import APIRouter, Depends
from dashboard.backend.schemas import Ability
from typing import List
from dashboard.backend.database import get_abilities, update_abilities_by_progress
from dashboard.backend.auth.dependencies import get_current_user

router = APIRouter(prefix="/api/abilities", tags=["能力"])


@router.get("", response_model=List[Ability])
async def get_abilities_list(current_user: dict = Depends(get_current_user)):
    """获取用户能力列表"""
    update_abilities_by_progress(user_id=current_user["user_id"])
    abilities = get_abilities(user_id=current_user["user_id"])
    return abilities


@router.get("/phases")
async def get_abilities_by_phase(current_user: dict = Depends(get_current_user)):
    """按阶段获取能力分组"""
    update_abilities_by_progress(user_id=current_user["user_id"])
    abilities = get_abilities(user_id=current_user["user_id"])

    phases = {}
    for a in abilities:
        phase = a["phase"]
        if phase not in phases:
            phases[phase] = []
        phases[phase].append(a)

    return phases