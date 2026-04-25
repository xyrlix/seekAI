"""
任务 57：损失函数

任务要求：
1. 创建预测值和真实值
2. 分别计算不同损失函数的值
3. 对比回归和分类任务的损失函数
4. 分析各损失函数的适用场景
5. 自定义一个简单的损失函数

知识点：
- MSELoss, L1Loss, SmoothL1Loss
- CrossEntropyLoss, NLLLoss
- 损失函数选择
- 自定义损失

难度：⭐⭐⭐
"""

import torch
import torch.nn as nn

# TODO: 1. 创建预测值和真实值
# 回归任务：pred 和 target 为连续值
# 分类任务：pred 为 logits，target 为类别索引
# 在此处写代码


# TODO: 2. 计算回归损失
# - MSELoss（均方误差）
# - L1Loss（平均绝对误差）
# - SmoothL1Loss
# 比较三者差异
# 在此处写代码


# TODO: 3. 计算分类损失
# - CrossEntropyLoss
# - NLLLoss
# 注意输入格式要求
# 在此处写代码


# TODO: 4. 分析各损失函数适用场景
# 用注释说明：
# - 回归任务选哪个？为什么？
# - 二分类选哪个？
# - 多分类选哪个？
# 在此处写注释


# TODO: 5. 自定义损失函数
# 创建一个简单的自定义损失（如：加权 MSE）
# 继承 nn.Module
# 在此处写代码
