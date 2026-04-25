"""
任务 54：训练循环编写

任务要求：
1. 定义通用的训练函数（可复用于不同模型）
2. 定义通用的评估函数
3. 实现多轮训练循环
4. 记录并打印每轮的损失和准确率
5. 保存最佳模型

知识点：
- 训练循环设计
- 训练/评估模式切换
- 模型保存与加载
- 训练过程监控

难度：⭐⭐⭐⭐
"""

import torch
import torch.nn as nn

# TODO: 1. 定义训练函数
# def train_one_epoch(model, dataloader, criterion, optimizer, device)
# 返回平均损失
# 在此处写代码


# TODO: 2. 定义评估函数
# def evaluate(model, dataloader, criterion, device)
# 返回平均损失和准确率
# 在此处写代码


# TODO: 3. 实现多轮训练循环
# def train_model(model, train_loader, val_loader, num_epochs)
# 每轮调用 train_one_epoch 和 evaluate
# 在此处写代码


# TODO: 4. 记录训练历史
# 使用列表或字典保存每轮的 loss 和 accuracy
# 打印训练进度
# 在此处写代码


# TODO: 5. 保存最佳模型
# 当验证集准确率最高时保存模型
# 使用 torch.save()
# 在此处写代码


# TODO: 6. 加载保存的模型
# 使用 torch.load()
# 验证模型是否正确加载
# 在此处写代码
