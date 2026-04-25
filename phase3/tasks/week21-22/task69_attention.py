"""
任务 69：Attention 机制

任务要求：
1. 实现简单的 Attention 函数
2. 理解 Q, K, V 的概念
3. 计算注意力权重
4. 可视化注意力分布
5. 解释 Attention 的优势

知识点：
- Attention 机制
- Query, Key, Value
- 注意力权重
- 加权求和

难度：⭐⭐⭐⭐
"""

import torch
import torch.nn as nn

# TODO: 1. 实现简单 Attention 函数
# def attention(query, key, value):
#     scores = query @ key.transpose(-2, -1)
#     weights = torch.softmax(scores, dim=-1)
#     return weights @ value, weights
# 在此处写代码


# TODO: 2. 创建 Q, K, V 张量
# query, key, value 形状一致
# 如：(batch, seq_len, dim)
# 在此处写代码


# TODO: 3. 计算注意力权重
# 调用 attention 函数
# 查看输出权重和结果
# 在此处写代码


# TODO: 4. 可视化注意力分布
# 使用热力图显示注意力权重
# 分析哪些位置获得更多关注
# 在此处写代码


# TODO: 5. 解释 Attention 的优势
# 用注释说明：
# - 相比 RNN 的优势
# - 为什么适合并行计算？
# - Attention 在哪些任务中表现好？
# 在此处写注释
