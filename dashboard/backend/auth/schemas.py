"""
认证模块 Pydantic 模型
"""

from pydantic import BaseModel, field_validator
from typing import Optional
import re


class UserRegister(BaseModel):
    """注册请求"""
    email: str
    password: str
    name: str

    @field_validator('email')
    @classmethod
    def validate_email(cls, v):
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', v):
            raise ValueError('Invalid email format')
        return v

    @field_validator('password')
    @classmethod
    def validate_password(cls, v):
        if len(v) < 6:
            raise ValueError('Password must be at least 6 characters')
        return v


class UserLogin(BaseModel):
    """登录请求"""
    email: str
    password: str


class TokenResponse(BaseModel):
    """令牌响应"""
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int = 900  # 15 minutes


class RefreshRequest(BaseModel):
    """刷新令牌请求"""
    refresh_token: str


class UserResponse(BaseModel):
    """用户信息响应"""
    id: int
    email: str
    name: str
    is_admin: bool = False
    oauth_provider: Optional[str] = None


class OAuthCallback(BaseModel):
    """OAuth 回调数据（内部使用）"""
    provider: str  # 'google' or 'github'
    code: str
    state: Optional[str] = None