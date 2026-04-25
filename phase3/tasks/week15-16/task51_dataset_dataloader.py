"""
任务 51：Dataset 和 DataLoader

任务要求：
1. 自定义一个 Dataset 类
2. 实现 __len__ 和 __getitem__ 方法
3. 使用 DataLoader 加载数据
4. 设置 batch_size 和 shuffle
5. 遍历 DataLoader 并输出数据

知识点：
- torch.utils.data.Dataset
- torch.utils.data.DataLoader
- 自定义数据集
- 批量加载

难度：⭐⭐⭐
"""

import torch
from torch.utils.data import Dataset, DataLoader

# TODO: 1. 自定义 Dataset 类
# 创建一个简单的数字数据集类
# 继承 Dataset，实现 __init__, __len__, __getitem__
# 在此处写代码


# TODO: 2. 实例化 Dataset
# 创建 100 个样本的数据集
# 测试 __len__ 和 __getitem__
# 在此处写代码


# TODO: 3. 创建 DataLoader
# batch_size=10, shuffle=True
# 在此处写代码


# TODO: 4. 遍历 DataLoader
# 打印每个 batch 的形状和内容
# 查看总共多少个 batch
# 在此处写代码


# TODO: 5. 尝试不同的 DataLoader 参数
# - num_workers: 多进程加载
# - drop_last: 是否丢弃最后一个不完整的 batch
# 观察差异
# 在此处写代码
