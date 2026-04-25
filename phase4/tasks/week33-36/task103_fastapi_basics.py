"""
任务 103：FastAPI 基础

任务要求：
1. 理解 FastAPI 框架
2. 创建简单的 API 服务
3. 实现 GET 和 POST 请求
4. 添加请求体和响应体模型
5. 使用 Swagger UI 测试 API

知识点：
- FastAPI 基础
- HTTP 请求方法
- Pydantic 模型
- Swagger UI

难度：⭐⭐⭐⭐
"""

from fastapi import FastAPI
from pydantic import BaseModel

# TODO: 1. 解释 FastAPI
# 用注释说明：
# - 什么是 FastAPI？
# - 相比 Flask 的优势
# - 适用场景
# 在此处写注释


# TODO: 2. 创建 FastAPI 应用
# app = FastAPI()
# 创建基础路由
# @app.get("/")
# 在此处写代码


# TODO: 3. 实现 GET 请求
# 创建多个 GET 接口
# 如：/users, /users/{user_id}
# 返回 JSON 数据
# 在此处写代码


# TODO: 4. 实现 POST 请求
# 定义请求体模型（使用 Pydantic）
# class Item(BaseModel):
#     name: str
#     price: float
# 创建 POST /items/ 接口
# 在此处写代码


# TODO: 5. 启动和测试
# 运行：uvicorn main:app --reload
# 访问 http://localhost:8000/docs 查看 Swagger UI
# 测试各接口
# 在此处写注释
