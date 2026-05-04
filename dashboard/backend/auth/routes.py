"""
认证路由 - 注册/登录/OAuth
"""

from fastapi import APIRouter, Depends, HTTPException, status, Query
from fastapi.responses import RedirectResponse
import os

from .schemas import UserRegister, UserLogin, TokenResponse, RefreshRequest, UserResponse
from .service import (
    hash_password, verify_password, create_access_token, create_refresh_token,
    verify_refresh_token, get_oauth_authorization_url, exchange_oauth_code
)
from .dependencies import get_current_user
from ..database import get_connection

router = APIRouter(prefix="/api/auth", tags=["认证"])


@router.post("/register", response_model=TokenResponse)
async def register(data: UserRegister):
    """注册新用户"""
    conn = get_connection()
    cursor = conn.cursor()

    # Check if email exists
    cursor.execute("SELECT id FROM auth_users WHERE email = ?", (data.email,))
    if cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create user
    password_hash = hash_password(data.password)
    cursor.execute("""
        INSERT INTO auth_users (email, password_hash, name, created_at)
        VALUES (?, ?, ?, datetime('now'))
    """, (data.email, password_hash, data.name))

    user_id = cursor.lastrowid
    conn.commit()
    conn.close()

    # Generate tokens
    access_token = create_access_token(user_id, data.email)
    refresh_token = create_refresh_token(user_id)

    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token,
        expires_in=900
    )


@router.post("/login", response_model=TokenResponse)
async def login(data: UserLogin):
    """用户登录"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, email, password_hash, name FROM auth_users
        WHERE email = ? AND password_hash IS NOT NULL
    """, (data.email,))

    row = cursor.fetchone()
    conn.close()

    if not row or not verify_password(data.password, row[2]):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    user_id, email, _, name = row

    # Update last login
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE auth_users SET last_login = datetime('now') WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()

    # Generate tokens
    access_token = create_access_token(user_id, email)
    refresh_token = create_refresh_token(user_id)

    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token,
        expires_in=900
    )


@router.post("/refresh", response_model=TokenResponse)
async def refresh(data: RefreshRequest):
    """刷新访问令牌"""
    user_id = verify_refresh_token(data.refresh_token)

    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT email FROM auth_users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()

    if not row:
        raise HTTPException(status_code=401, detail="User not found")

    email = row[0]

    access_token = create_access_token(user_id, email)
    new_refresh_token = create_refresh_token(user_id)

    return TokenResponse(
        access_token=access_token,
        refresh_token=new_refresh_token,
        expires_in=900
    )


@router.post("/logout")
async def logout(current_user: dict = Depends(get_current_user)):
    """用户登出（客户端应删除令牌）"""
    return {"message": "Logged out successfully"}


@router.get("/me", response_model=UserResponse)
async def get_me(current_user: dict = Depends(get_current_user)):
    """获取当前用户信息"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, email, name, is_admin, oauth_provider
        FROM auth_users WHERE id = ?
    """, (current_user["user_id"],))

    row = cursor.fetchone()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="User not found")

    return UserResponse(
        id=row[0],
        email=row[1],
        name=row[2],
        is_admin=bool(row[3]),
        oauth_provider=row[4]
    )


# OAuth2 Routes
@router.get("/oauth/{provider}")
async def oauth_login(provider: str):
    """OAuth2 登录入口"""
    if provider not in ["google", "github"]:
        raise HTTPException(status_code=400, detail="Unsupported provider")

    url = get_oauth_authorization_url(provider)
    if not url:
        raise HTTPException(status_code=400, detail=f"{provider} OAuth not configured")

    return RedirectResponse(url)


@router.get("/oauth/{provider}/callback")
async def oauth_callback(provider: str, code: str = Query(...), state: str = Query(None)):
    """OAuth2 回调处理"""
    if provider not in ["google", "github"]:
        raise HTTPException(status_code=400, detail="Unsupported provider")

    user_info = await exchange_oauth_code(provider, code)
    if not user_info:
        raise HTTPException(status_code=400, detail="OAuth authentication failed")

    conn = get_connection()
    cursor = conn.cursor()

    # Check if user exists via OAuth
    cursor.execute("""
        SELECT id, email, name, is_admin FROM auth_users
        WHERE oauth_provider = ? AND oauth_id = ?
    """, (provider, user_info["oauth_id"]))

    row = cursor.fetchone()

    if row:
        # Existing OAuth user
        user_id, email, name, is_admin = row
    else:
        # Create new OAuth user
        cursor.execute("""
            INSERT INTO auth_users (email, name, oauth_provider, oauth_id, created_at)
            VALUES (?, ?, ?, ?, datetime('now'))
        """, (user_info["email"], user_info["name"], provider, user_info["oauth_id"]))
        user_id = cursor.lastrowid
        email = user_info["email"]
        name = user_info["name"]
        is_admin = False

    conn.commit()
    conn.close()

    # Generate tokens
    access_token = create_access_token(user_id, email)
    refresh_token = create_refresh_token(user_id)

    # Redirect to frontend with token (simplified)
    frontend_url = os.getenv("FRONTEND_URL", "http://localhost:5173")
    return RedirectResponse(
        f"{frontend_url}/auth/callback?access_token={access_token}&refresh_token={refresh_token}"
    )