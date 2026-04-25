"""
任务 50：自动微分（Autograd）

任务要求：
1. 创建 requires_grad=True 的 Tensor
2. 进行一系列运算并查看计算图
3. 调用 backward() 计算梯度
4. 查看各变量的梯度值
5. 使用 torch.no_grad() 禁用梯度追踪

知识点：
- 自动微分原理
- requires_grad
- backward()
- .grad 属性
- torch.no_grad()

难度：⭐⭐⭐
"""

import torch

# TODO: 1. 创建需要梯度的 Tensor
# x = torch.tensor(2.0, requires_grad=True)
# y = torch.tensor(3.0, requires_grad=True)
# 在此处写代码


# TODO: 2. 进行运算构建计算图
# z = x ** 2 + 2 * x * y + y ** 2
# 查看 z 的 grad_fn 属性
# 在此处写代码


# TODO: 3. 反向传播计算梯度
# z.backward()
# 打印 x.grad 和 y.grad
# 验证是否正确（手动计算导数对比）
# 在此处写代码


# TODO: 4. 更复杂的梯度计算
# 定义一个简单的神经网络前向传播
# 计算损失并反向传播
# 在此处写代码


# TODO: 5. 使用 torch.no_grad() 禁用梯度追踪
# 在推理时不需要计算梯度
# 比较使用和不使用时的内存和速度差异
# 在此处写代码
