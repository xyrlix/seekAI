"""
任务 30：房价预测项目

任务要求：
1. 创建一个完整的房价预测数据集（包含多个特征）
2. 划分训练集和测试集
3. 训练线性回归模型
4. 在测试集上评估模型（使用 MSE 和 R²）
5. 预测 2 个新房的价格并输出

知识点：
- 多特征数据集构建
- 完整的 ML 流程
- mean_squared_error, r2_score
- 端到端项目实践

难度：⭐⭐⭐⭐
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# TODO: 1. 创建房价数据集
# 特征：面积(㎡), 房间数, 房龄(年), 距离市中心距离(km)
# 创建至少 50 个样本的数据
# 在此处写代码


# TODO: 2. 划分数据集
# 测试集占 20%，random_state=42
# 在此处写代码


# TODO: 3. 训练模型
# 使用 LinearRegression
# 在此处写代码


# TODO: 4. 评估模型
# 使用 mean_squared_error 和 r2_score
# 在此处写代码


# TODO: 5. 预测新房价格
# 新房1: 100㎡, 3 房间, 5 年房龄, 距离 10km
# 新房2: 80㎡, 2 房间, 10 年房龄, 距离 15km
# 在此处写代码
