"""
任务 59：图片分类器

任务要求：
1. 使用 CIFAR-10 数据集
2. 构建一个适合图片分类的网络
3. 完整训练流程（多轮训练）
4. 在测试集上评估
5. 可视化预测结果

知识点：
- CIFAR-10 数据集
- 图片分类网络设计
- 完整训练流程
- 结果可视化

难度：⭐⭐⭐⭐
"""

import torch
import torch.nn as nn
from torchvision import datasets, transforms
import matplotlib.pyplot as plt

# TODO: 1. 加载 CIFAR-10 数据集
# 定义 transforms（归一化）
# 创建 train 和 test DataLoader
# 类别名称：['airplane', 'automobile', 'bird', 'cat', 'deer',
#            'dog', 'frog', 'horse', 'ship', 'truck']
# 在此处写代码


# TODO: 2. 构建图片分类网络
# 输入：3x32x32（RGB 图片）
# 输出：10 个类别
# 使用卷积层或全连接层
# 在此处写代码


# TODO: 3. 定义训练流程
# - 损失函数和优化器
# - 训练多轮（如 5 轮）
# - 每轮打印损失
# 在此处写代码


# TODO: 4. 在测试集上评估
# - 计算整体准确率
# - 计算每个类别的准确率
# 在此处写代码


# TODO: 5. 可视化预测结果
# 随机选择 10 张图片
# 显示图片及预测结果
# 用不同颜色标注正确/错误预测
# 在此处写代码
