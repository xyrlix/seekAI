"""
任务 52：简单神经网络

任务要求：
1. 使用 nn.Module 定义一个简单的神经网络
2. 网络包含 2 个全连接层
3. 定义损失函数和优化器
4. 进行一次前向传播和反向传播
5. 查看网络参数

知识点：
- nn.Module
- nn.Linear
- 损失函数和优化器
- 前向传播和反向传播

难度：⭐⭐⭐
"""

import torch
import torch.nn as nn
import torch.optim as optim

# TODO: 1. 定义神经网络类
# 继承 nn.Module
# __init__ 中定义层
# forward 方法定义前向传播
# 输入维度 10，隐藏层 20，输出维度 2
# 在此处写代码


# TODO: 2. 实例化网络并查看结构
# print(model)
# 查看网络参数
# 在此处写代码


# TODO: 3. 创建示例输入数据
# batch_size=4, input_dim=10
# 进行前向传播
# 在此处写代码


# TODO: 4. 定义损失函数和优化器
# 使用 MSELoss 或 CrossEntropyLoss
# 使用 SGD 或 Adam 优化器
# 在此处写代码


# TODO: 5. 进行一次完整的训练步骤
# - 前向传播
# - 计算损失
# - 反向传播（loss.backward()）
# - 更新参数（optimizer.step()）
# - 梯度清零（optimizer.zero_grad()）
# 在此处写代码
