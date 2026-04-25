"""
任务 78：模型训练调试实战

任务要求：
1. 给定一个有 bug 的训练代码
2. 诊断并修复问题
3. 解决训练不收敛的问题
4. 优化训练流程
5. 编写调试检查清单

知识点：
- 常见训练问题排查
- 调试技巧
- 训练流程检查
- 最佳实践总结

难度：⭐⭐⭐⭐⭐
"""

import torch
import torch.nn as nn

# TODO: 1. 诊断训练代码中的常见 bug
# 检查以下代码的问题并修复：
# （故意给出有问题的代码）
#
# model = nn.Linear(10, 2)
# optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
# criterion = nn.MSELoss()
#
# for epoch in range(100):
#     output = model(inputs)
#     loss = criterion(output, targets)
#     loss.backward()
#     optimizer.step()
#     # 缺少 optimizer.zero_grad()
#
# 在此处写修复后的代码


# TODO: 2. 解决训练不收敛问题
# 检查以下可能原因：
# - 学习率是否合适？
# - 数据是否正确归一化？
# - 标签是否正确？
# - 损失函数是否正确？
# 逐一排查
# 在此处写代码和注释


# TODO: 3. 创建训练调试工具函数
# def debug_training(model, dataloader):
#     - 检查梯度是否为 NaN
#     - 检查权重是否更新
#     - 打印各层梯度范数
# 在此处写代码


# TODO: 4. 编写调试检查清单
# 训练不收敛时依次检查：
# 1. 数据是否正确？
# 2. 学习率是否合适？
# 3. 损失函数是否正确？
# 4. 梯度是否正常？
# 5. ...
# 在此处写注释


# TODO: 5. 总结调试经验
# 记录遇到的问题及解决方案
# 形成个人调试经验库
# 在此处写注释
