"""
任务 65：CIFAR-10 图片分类

任务要求：
1. 使用 CIFAR-10 数据集
2. 构建或改进 CNN 模型
3. 完整训练流程（多轮）
4. 在测试集上达到至少 60% 准确率
5. 分析错误预测案例

知识点：
- CIFAR-10 数据集
- CNN 图片分类
- 数据增强
- 错误分析

难度：⭐⭐⭐⭐
"""

import torch
import torch.nn as nn
from torchvision import datasets, transforms

# TODO: 1. 加载 CIFAR-10 数据集
# 使用数据增强（随机裁剪、翻转等）
# transforms.RandomCrop, transforms.RandomHorizontalFlip
# 在此处写代码


# TODO: 2. 构建 CNN 模型
# 设计适合 CIFAR-10 的网络
# 建议：多层 Conv + Pool + FC
# 在此处写代码


# TODO: 3. 训练模型
# 训练 5-10 轮
# 每轮打印训练和验证准确率
# 在此处写代码


# TODO: 4. 评估模型
# 在测试集上计算准确率
# 计算每个类别的准确率
# 找出最难分类的类别
# 在此处写代码


# TODO: 5. 分析错误案例
# 随机选择一些预测错误的图片
# 显示图片、真实标签和预测标签
# 分析错误原因
# 在此处写代码
