"""
任务 104：AI 模型 API 封装

任务要求：
1. 将训练好的 ML 模型封装为 API
2. 实现模型预测接口
3. 添加输入验证
4. 实现批量预测
5. 测试 API 性能

知识点：
- 模型部署
- API 设计
- 输入验证
- 性能测试

难度：⭐⭐⭐⭐
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# TODO: 1. 加载训练好的模型
# 使用 joblib 或 torch.load 加载模型
# 加载预处理器（scaler 等）
# 在此处写代码


# TODO: 2. 定义请求和响应模型
# class PredictionRequest(BaseModel):
#     features: list[float]
# class PredictionResponse(BaseModel):
#     prediction: int
#     probability: float
# 在此处写代码


# TODO: 3. 实现预测接口
# POST /predict
# - 接收特征数据
# - 预处理
# - 模型预测
# - 返回结果
# 在此处写代码


# TODO: 4. 实现批量预测
# POST /predict/batch
# 接收多个样本
# 批量预测并返回结果
# 在此处写代码


# TODO: 5. 性能测试
# 使用工具测试：
# - 响应时间
# - 并发处理能力
# - 内存使用
# 输出性能报告
# 在此处写代码
