"""
任务 67：循环神经网络（RNN）

任务要求：
1. 创建 RNN 层并理解各参数
2. 对序列数据进行前向传播
3. 查看隐藏状态输出
4. 解释 RNN 的工作原理
5. 在简单序列数据上应用

知识点：
- nn.RNN
- 隐藏状态
- 序列数据格式
- 时间步

难度：⭐⭐⭐
"""

import torch
import torch.nn as nn

# TODO: 1. 创建 RNN 层
# nn.RNN(input_size, hidden_size, num_layers, batch_first)
# 理解各参数含义
# 在此处写代码


# TODO: 2. 创建序列输入数据
# 形状：(seq_len, batch, input_size) 或 (batch, seq_len, input_size)
# 如：10 个时间步，5 个样本，每个特征 20
# 在此处写代码


# TODO: 3. 前向传播
# output, hidden = rnn(input)
# 查看 output 和 hidden 的形状
# 解释两者的区别
# 在此处写代码


# TODO: 4. 用注释解释 RNN 工作原理
# - 隐藏状态如何传递？
# - 为什么适合序列数据？
# - RNN 的局限性是什么？
# 在此处写注释


# TODO: 5. 应用简单序列预测
# 如：正弦波预测
# 训练 RNN 预测下一个值
# 在此处写代码
