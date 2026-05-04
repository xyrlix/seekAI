"""
认证依赖 - FastAPI Depends
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Optional

from .service import verify_access_token

security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> dict:
    """获取当前用户（需要 Bearer token）"""
    token = credentials.credentials
    result = verify_access_token(token)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user_id, email = result
    return {"user_id": user_id, "email": email}


async def get_optional_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(HTTPBearer(auto_error=False))
) -> Optional[dict]:
    """获取当前用户（可选，不存在则返回 None）"""
    if not credentials:
        return None

    token = credentials.credentials
    result = verify_access_token(token)

    if not result:
        return None

    user_id, email = result
    return {"user_id": user_id, "email": email}


async def get_admin_user(
    current_user: dict = Depends(get_current_user),
) -> dict:
    """获取管理员用户"""
    from ..database import get_connection

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT is_admin FROM auth_users WHERE id = ?", (current_user["user_id"],))
    row = cursor.fetchone()
    conn.close()

    if not row or not row[0]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )

    return current_user