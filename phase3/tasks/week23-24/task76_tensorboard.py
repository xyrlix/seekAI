"""
任务 76：TensorBoard 可视化

任务要求：
1. 安装和配置 TensorBoard
2. 使用 SummaryWriter 记录训练指标
3. 可视化损失曲线和准确率
4. 可视化网络结构和直方图
5. 启动 TensorBoard 查看结果

知识点：
- TensorBoard
- SummaryWriter
- 训练可视化
- 日志管理

难度：⭐⭐⭐
"""

import torch
import torch.nn as nn
from torch.utils.tensorboard import SummaryWriter

# TODO: 1. 创建 SummaryWriter
# writer = SummaryWriter('runs/experiment1')
# 指定日志目录
# 在此处写代码


# TODO: 2. 记录标量指标
# 在训练过程中使用 writer.add_scalar()
# 记录：loss, accuracy
# writer.add_scalar('Loss/train', loss, epoch)
# 在此处写代码


# TODO: 3. 可视化网络结构
# 使用 writer.add_graph()
# 需要传入模型和示例输入
# 在此处写代码


# TODO: 4. 记录权重直方图
# 使用 writer.add_histogram()
# 记录模型参数分布
# 在此处写代码


# TODO: 5. 启动 TensorBoard
# 在终端运行：tensorboard --logdir=runs
# 打开浏览器查看
# 用注释说明如何启动和访问
# 在此处写注释
