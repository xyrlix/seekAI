"""
任务 73：学习率调度器（Learning Rate Scheduler）

任务要求：
1. 创建简单模型和数据集
2. 使用不同学习率调度器
   - StepLR
   - ReduceLROnPlateau
   - CosineAnnealingLR
3. 绘制学习率变化曲线
4. 比较使用调度器与固定学习率的训练效果

知识点：
- 学习率调度
- StepLR, ReduceLROnPlateau, CosineAnnealingLR
- 学习率策略
- 训练优化

难度：⭐⭐⭐
"""

import torch
import torch.nn as nn
from torch.optim.lr_scheduler import StepLR, ReduceLROnPlateau, CosineAnnealingLR

# TODO: 1. 创建简单模型和优化器
# 简单分类模型
# 使用 Adam 或 SGD 优化器
# 在此处写代码


# TODO: 2. 使用 StepLR 调度器
# step_size=10, gamma=0.1
# 每 10 轮将学习率乘以 0.1
# 记录每轮的学习率
# 在此处写代码


# TODO: 3. 使用 ReduceLROnPlateau
# 当验证集损失不再下降时降低学习率
# patience=3, factor=0.5
# 在此处写代码


# TODO: 4. 使用 CosineAnnealingLR
# T_max=epochs
# 学习率按余弦曲线衰减
# 在此处写代码


# TODO: 5. 绘制学习率变化曲线
# x 轴：训练轮数
# y 轴：学习率
# 对比不同调度器的曲线
# 在此处写代码
