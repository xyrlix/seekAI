"""
任务 68：LSTM 和 GRU

任务要求：
1. 创建 LSTM 和 GRU 网络
2. 比较 LSTM、GRU 和普通 RNN 的差异
3. 理解门控机制
4. 在序列数据上训练对比
5. 解释长短时记忆的原理

知识点：
- nn.LSTM
- nn.GRU
- 门控机制
- 长程依赖

难度：⭐⭐⭐⭐
"""

import torch
import torch.nn as nn

# TODO: 1. 创建 LSTM 层
# nn.LSTM(input_size, hidden_size, num_layers)
# 查看 LSTM 的参数
# 在此处写代码


# TODO: 2. 创建 GRU 层
# nn.GRU(input_size, hidden_size, num_layers)
# 对比 LSTM 和 GRU 的参数数量
# 在此处写代码


# TODO: 3. 前向传播
# LSTM 输出：output, (hidden, cell)
# GRU 输出：output, hidden
# 查看各输出的形状
# 在此处写代码


# TODO: 4. 比较三者在序列数据上的表现
# 在同一任务上训练 RNN, LSTM, GRU
# 对比收敛速度和最终准确率
# 在此处写代码


# TODO: 5. 解释门控机制
# 用注释说明：
# - LSTM 的遗忘门、输入门、输出门
# - GRU 的更新门和重置门
# - 为什么能解决长程依赖问题？
# 在此处写注释
