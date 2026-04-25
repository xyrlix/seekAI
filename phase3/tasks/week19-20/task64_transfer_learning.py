"""
任务 64：迁移学习

任务要求：
1. 加载预训练的 ResNet 模型
2. 修改最后的全连接层适配新任务
3. 冻结部分层，只训练部分层
4. 在新数据集上训练
5. 比较迁移学习和从头训练的效果

知识点：
- 迁移学习概念
- torchvision.models
- 模型加载和修改
- 冻结参数

难度：⭐⭐⭐⭐
"""

import torch
import torch.nn as nn
from torchvision import models

# TODO: 1. 加载预训练模型
# 使用 torchvision.models.resnet18(pretrained=True)
# 打印网络结构
# 在此处写代码


# TODO: 2. 修改最后的全连接层
# 将输出类别数改为你需要的数量
# 如：model.fc = nn.Linear(in_features, num_classes)
# 在此处写代码


# TODO: 3. 冻结部分参数
# 冻结除最后全连接层外的所有参数
# 遍历 model.named_parameters()
# 设置 requires_grad = False
# 在此处写代码


# TODO: 4. 在新数据集上训练
# 使用简单的数据集
# 只训练未冻结的参数
# 在此处写代码


# TODO: 5. 比较迁移学习和从头训练
# - 训练时间
# - 收敛速度
# - 最终准确率
# 用注释记录对比结果
# 在此处写代码和注释
