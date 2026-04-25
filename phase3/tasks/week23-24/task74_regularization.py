"""
任务 74：正则化

任务要求：
1. 创建一个容易过拟合的模型（如大网络 + 小数据）
2. 实现 L2 正则化（Weight Decay）
3. 实现 Dropout
4. 实现 Batch Normalization
5. 对比各正则化方法的效果

知识点：
- 过拟合与欠拟合
- L2 正则化
- Dropout
- Batch Normalization

难度：⭐⭐⭐
"""

import torch
import torch.nn as nn

# TODO: 1. 创建容易过拟合的场景
# - 小数据集（如 100 个样本）
# - 大网络（如 5 层，每层 256 个神经元）
# 训练并观察过拟合现象
# 在此处写代码


# TODO: 2. 添加 L2 正则化
# 在优化器中设置 weight_decay
# 如：Adam(model.parameters(), lr=0.001, weight_decay=1e-4)
# 观察训练效果
# 在此处写代码


# TODO: 3. 添加 Dropout
# 在网络中添加 nn.Dropout(p=0.5)
# 训练并观察效果
# 注意：训练时启用，评估时禁用
# 在此处写代码


# TODO: 4. 添加 Batch Normalization
# 在网络中添加 nn.BatchNorm1d
# 观察对训练的影响
# 在此处写代码


# TODO: 5. 对比各正则化方法
# 输出对比表格：
# 方法 | 训练准确率 | 验证准确率 | 差距
# 分析哪种方法最有效
# 在此处写代码
