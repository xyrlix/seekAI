"""
任务 72：简单翻译模型

任务要求：
1. 创建简单的英-中翻译数据集
2. 构建 Seq2Seq 模型（Encoder-Decoder）
3. 实现注意力机制
4. 训练翻译模型
5. 测试翻译效果

知识点：
- Seq2Seq 架构
- Encoder-Decoder
- 机器翻译
- 注意力机制应用

难度：⭐⭐⭐⭐⭐
"""

import torch
import torch.nn as nn

# TODO: 1. 创建翻译数据集
# 简单句子对：
# 'hello' -> '你好'
# 'thank you' -> '谢谢'
# 构建词表
# 在此处写代码


# TODO: 2. 构建 Encoder
# 使用 LSTM 或 GRU
# 将输入序列编码为隐藏状态
# 在此处写代码


# TODO: 3. 构建 Decoder
# 使用 LSTM 或 GRU
# 根据编码生成目标序列
# 在此处写代码


# TODO: 4. 训练翻译模型
# 使用 teacher forcing
# 训练多轮
# 记录损失
# 在此处写代码


# TODO: 5. 测试翻译
# 输入新句子
# 使用贪心解码或 beam search
# 输出翻译结果
# 在此处写代码
