"""
任务 53：MNIST 手写数字识别

任务要求：
1. 加载 MNIST 数据集
2. 构建一个神经网络（至少 2 层）
3. 实现训练函数
4. 训练 1 个 epoch 并输出损失
5. 在测试集上评估准确率

知识点：
- torchvision.datasets.MNIST
- 图像数据预处理
- 训练流程
- 模型评估

难度：⭐⭐⭐⭐
"""

import torch
import torch.nn as nn
from torchvision import datasets, transforms

# TODO: 1. 加载 MNIST 数据集
# 使用 torchvision.datasets.MNIST
# 定义 transforms（归一化）
# 创建 DataLoader
# 在此处写代码


# TODO: 2. 定义神经网络
# 输入 28*28=784，输出 10（0-9 数字）
# 使用 2-3 个全连接层
# 在此处写代码


# TODO: 3. 定义训练函数
# - 遍历训练 DataLoader
# - 前向传播 + 计算损失 + 反向传播 + 更新参数
# - 打印每个 batch 的损失
# 在此处写代码


# TODO: 4. 训练 1 个 epoch
# 调用训练函数
# 在此处写代码


# TODO: 5. 在测试集上评估
# - 切换到 eval 模式
# - 计算准确率
# - 输出结果
# 在此处写代码
