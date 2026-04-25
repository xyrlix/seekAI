"""
任务 61：卷积层（Convolution Layer）

任务要求：
1. 创建 2D 卷积层并理解各参数
2. 对输入图像应用卷积操作
3. 查看输出特征图的形状
4. 可视化卷积核和卷积结果
5. 解释卷积的工作原理

知识点：
- nn.Conv2d
- 卷积核、步幅、填充
- 输入输出通道
- 特征图

难度：⭐⭐⭐
"""

import torch
import torch.nn as nn

# TODO: 1. 创建 2D 卷积层
# nn.Conv2d(in_channels, out_channels, kernel_size, stride, padding)
# 理解各参数含义
# 在此处写代码


# TODO: 2. 创建输入图像
# 形状为 (batch, channels, height, width)
# 如：(1, 3, 32, 32)
# 在此处写代码


# TODO: 3. 应用卷积操作
# 输出特征图并查看形状
# 验证输出形状计算公式：
# output = (input + 2*padding - kernel_size) / stride + 1
# 在此处写代码


# TODO: 4. 尝试不同参数
# - 改变 kernel_size（3, 5, 7）
# - 改变 stride（1, 2）
# - 改变 padding（0, 1, 2）
# 观察输出形状变化
# 在此处写代码


# TODO: 5. 用注释解释卷积工作原理
# - 卷积核如何滑动？
# - 填充的作用？
# - 多通道如何处理？
# 在此处写注释
