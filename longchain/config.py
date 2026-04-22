"""
LangChain 示例项目配置文件
从环境变量或 .env 文件中加载 API 配置
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# 加载 .env 文件
env_path = Path(__file__).parent / ".env"
if env_path.exists():
    load_dotenv(env_path)
    print(f"已加载配置文件: {env_path}")
else:
    print("未找到 .env 文件，使用环境变量或默认配置")


def get_llm_config():
    """获取大模型配置"""
    return {
        "model": os.getenv("MINIMAX_MODEL", "minimax-m2.7"),
        "api_key": os.getenv("MINIMAX_API_KEY", ""),
        "base_url": os.getenv("MINIMAX_BASE_URL", "https://api.minimax.chat/v1"),
    }


def create_llm(**kwargs):
    """创建 ChatOpenAI 实例"""
    from langchain_openai import ChatOpenAI
    
    config = {**get_llm_config(), **kwargs}
    
    if not config["api_key"]:
        raise ValueError(
            "未设置 MINIMAX_API_KEY 环境变量！\n"
            "请复制 .env.example 为 .env 并填入你的 API 密钥"
        )
    
    return ChatOpenAI(
        model=config["model"],
        api_key=config["api_key"],
        base_url=config["base_url"],
    )
