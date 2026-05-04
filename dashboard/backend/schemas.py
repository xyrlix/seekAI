"""
Pydantic 数据模型
"""

from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class TaskBase(BaseModel):
    """任务基础模型"""
    id: int
    phase: int
    week: int
    name: str


class Task(TaskBase):
    """任务完整模型"""
    status: str = "pending"
    score: Optional[int] = None
    completed_at: Optional[str] = None


class TaskList(BaseModel):
    """任务列表响应"""
    tasks: List[Task]
    total: int
    completed: int


class ReviewRequest(BaseModel):
    """评分请求"""
    task_id: int
    correctness: int
    conventions: int
    performance: int
    readability: int


class ReviewResponse(BaseModel):
    """评分响应"""
    total: int
    passed: bool


class ProgressResponse(BaseModel):
    """进度响应"""
    total: int
    completed: int
    avg_score: float
    phases: List[dict]


class StatsResponse(BaseModel):
    """统计信息响应"""
    total_tasks: int
    completed_tasks: int
    total_score: float
    current_streak: int  # 连续学习天数
    achievements_count: int


class Ability(BaseModel):
    """能力模型"""
    id: int
    name: str
    icon: str
    description: str
    level: int  # 0-100
    phase: int  # 对应Phase
