"""
认证服务 - JWT + OAuth2
"""

import os
import secrets
import hashlib
from datetime import datetime, timedelta
from typing import Optional, Tuple

from jose import JWTError, jwt
from passlib.context import CryptContext

# Password hashing
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

# JWT Settings
SECRET_KEY = os.getenv("SECRET_KEY", secrets.token_urlsafe(32))
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 7


def hash_password(password: str) -> str:
    """密码哈希"""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """验证密码"""
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(user_id: int, email: str) -> str:
    """创建访问令牌"""
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {
        "sub": str(user_id),
        "email": email,
        "exp": expire,
        "type": "access"
    }
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def create_refresh_token(user_id: int) -> str:
    """创建刷新令牌"""
    expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    token = secrets.token_urlsafe(32)
    # Store hash of token for verification
    token_hash = hashlib.sha256(token.encode()).hexdigest()
    to_encode = {
        "sub": str(user_id),
        "exp": expire,
        "type": "refresh",
        "jti": token_hash
    }
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str) -> Optional[dict]:
    """解码并验证令牌"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None


def verify_access_token(token: str) -> Optional[Tuple[int, str]]:
    """验证访问令牌，返回 (user_id, email)"""
    payload = decode_token(token)
    if not payload:
        return None
    if payload.get("type") != "access":
        return None
    try:
        user_id = int(payload.get("sub"))
        email = payload.get("email")
        return (user_id, email)
    except (ValueError, TypeError):
        return None


def verify_refresh_token(token: str) -> Optional[int]:
    """验证刷新令牌，返回 user_id"""
    payload = decode_token(token)
    if not payload:
        return None
    if payload.get("type") != "refresh":
        return None
    try:
        user_id = int(payload.get("sub"))
        return user_id
    except (ValueError, TypeError):
        return None


# OAuth2 配置
OAUTH_CONFIG = {
    "google": {
        "client_id": os.getenv("GOOGLE_CLIENT_ID", ""),
        "client_secret": os.getenv("GOOGLE_CLIENT_SECRET", ""),
        "authorize_url": "https://accounts.google.com/o/oauth2/v2/auth",
        "token_url": "https://oauth2.googleapis.com/token",
        "userinfo_url": "https://www.googleapis.com/oauth2/v2/userinfo",
    },
    "github": {
        "client_id": os.getenv("GITHUB_CLIENT_ID", ""),
        "client_secret": os.getenv("GITHUB_CLIENT_SECRET", ""),
        "authorize_url": "https://github.com/login/oauth/authorize",
        "token_url": "https://github.com/login/oauth/access_token",
        "userinfo_url": "https://api.github.com/user",
    }
}


def get_oauth_authorization_url(provider: str) -> Optional[str]:
    """获取 OAuth 授权 URL"""
    if provider not in OAUTH_CONFIG:
        return None

    config = OAUTH_CONFIG[provider]
    if not config["client_id"]:
        return None

    state = secrets.token_urlsafe(16)

    params = {
        "client_id": config["client_id"],
        "redirect_uri": f"{os.getenv('APP_URL', 'http://localhost:8000')}/api/auth/oauth/{provider}/callback",
        "scope": "openid email profile" if provider == "google" else "user:email",
        "response_type": "code",
        "state": state,
    }

    if provider == "google":
        params["access_type"] = "offline"
        params["prompt"] = "consent"

    query = "&".join(f"{k}={v}" for k, v in params.items())
    return f"{config['authorize_url']}?{query}"


async def exchange_oauth_code(provider: str, code: str) -> Optional[dict]:
    """交换 OAuth code 获取用户信息"""
    if provider not in OAUTH_CONFIG:
        return None

    import httpx

    config = OAUTH_CONFIG[provider]
    redirect_uri = f"{os.getenv('APP_URL', 'http://localhost:8000')}/api/auth/oauth/{provider}/callback"

    async with httpx.AsyncClient() as client:
        # Exchange code for token
        token_data = {
            "client_id": config["client_id"],
            "client_secret": config["client_secret"],
            "code": code,
            "redirect_uri": redirect_uri,
            "grant_type": "authorization_code",
        }

        if provider == "github":
            token_data["Accept"] = "application/json"

        try:
            response = await client.post(config["token_url"], data=token_data)
            token_response = response.json()

            if "access_token" not in token_response:
                return None

            access_token = token_response["access_token"]

            # Get user info
            headers = {"Authorization": f"Bearer {access_token}"}
            user_response = await client.get(config["userinfo_url"], headers=headers)
            user_info = user_response.json()

            return {
                "oauth_id": str(user_info.get("id")),
                "email": user_info.get("email"),
                "name": user_info.get("name") or user_info.get("login"),
                "provider": provider,
            }
        except Exception:
            return None