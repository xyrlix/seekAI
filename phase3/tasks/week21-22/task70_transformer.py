"""
任务 70：Transformer 基础

任务要求：
1. 使用 PyTorch 内置 Transformer
2. 理解 Transformer 的组成部分
3. 构建简单的位置编码
4. 实现前向传播
5. 解释 Self-Attention 和 Multi-Head Attention

知识点：
- nn.Transformer
- 位置编码
- Self-Attention
- Multi-Head Attention

难度：⭐⭐⭐⭐
"""

import torch
import torch.nn as nn

# TODO: 1. 创建位置编码
# 使用 nn.Embedding 或自定义正弦位置编码
# 位置编码 + 输入嵌入
# 在此处写代码


# TODO: 2. 使用 PyTorch Transformer
# nn.Transformer(d_model, nhead, num_encoder_layers)
# 理解各参数含义
# 在此处写代码


# TODO: 3. 构建源和目标序列
# src 和 tgt 形状：(seq_len, batch, d_model)
# 添加位置编码
# 在此处写代码


# TODO: 4. 前向传播
# output = transformer(src, tgt)
# 查看输出形状
# 在此处写代码


# TODO: 5. 解释 Transformer 核心组件
# 用注释说明：
# - Self-Attention vs Cross-Attention
# - Multi-Head Attention 的作用
# - 为什么需要位置编码？
# - Encoder 和 Decoder 的区别
# 在此处写注释
