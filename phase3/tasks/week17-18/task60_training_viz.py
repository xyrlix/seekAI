"""
任务 60：训练过程可视化

任务要求：
1. 训练一个简单的模型
2. 记录每轮的损失和准确率
3. 使用 matplotlib 绘制训练曲线
4. 分析训练曲线判断模型状态
5. 创建训练日志文件

知识点：
- 训练记录
- matplotlib 可视化
- 过拟合/欠拟合判断
- 训练日志

难度：⭐⭐⭐⭐
"""

import torch
import matplotlib.pyplot as plt

# TODO: 1. 训练模型并记录历史
# 在训练过程中保存：
# - train_loss, val_loss
# - train_acc, val_acc
# 使用字典或列表记录
# 在此处写代码


# TODO: 2. 绘制损失曲线
# 绘制训练集和验证集损失
# x 轴：epoch, y 轴：loss
# 两条线区分 train 和 val
# 在此处写代码


# TODO: 3. 绘制准确率曲线
# 绘制训练集和验证集准确率
# 同样区分 train 和 val
# 在此处写代码


# TODO: 4. 分析训练曲线
# 根据曲线判断：
# - 是否过拟合？（train 好，val 差）
# - 是否欠拟合？（train 和 val 都不好）
# - 训练是否充分？（曲线是否趋于平稳）
# 在此处写注释


# TODO: 5. 创建训练日志文件
# 将训练历史写入 txt 文件
# 包含：epoch, train_loss, val_loss, train_acc, val_acc
# 在此处写代码
