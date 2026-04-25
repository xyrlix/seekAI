"""
任务 105：RAG API 服务

任务要求：
1. 将 RAG 系统封装为 API 服务
2. 实现文档上传接口
3. 实现问答接口
4. 添加对话历史管理
5. 实现 API 鉴权

知识点：
- API 服务设计
- 文档管理
- 会话管理
- API 鉴权

难度：⭐⭐⭐⭐
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# TODO: 1. 设计 API 接口
# POST /documents/upload - 上传文档
# POST /documents/process - 处理文档
# POST /chat - 对话问答
# POST /chat/reset - 重置对话
# 用注释说明各接口功能
# 在此处写代码和注释


# TODO: 2. 实现文档上传
# 接收文档文件
# 存储到服务器
# 返回文档 ID
# 在此处写代码


# TODO: 3. 实现文档处理
# - 加载文档
# - 切分
# - 向量化
# - 存储到向量数据库
# 返回处理状态
# 在此处写代码


# TODO: 4. 实现问答接口
# 接收用户问题
# 调用 RAG 系统
# 返回答案和引用
# 保存对话历史
# 在此处写代码


# TODO: 5. 添加 API 鉴权
# 使用 API Key 鉴权
# 添加依赖项
# 保护敏感接口
# 在此处写代码
