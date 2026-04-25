"""
任务 39：交叉验证

任务要求：
1. 解释交叉验证的原理和优势
2. 使用 cross_val_score 进行 5 折交叉验证
3. 比较不同模型（决策树、随机森林、逻辑回归）的交叉验证得分
4. 使用 cross_validate 获取多个指标
5. 输出交叉验证的平均得分和标准差

知识点：
- 交叉验证概念（K-Fold）
- sklearn.model_selection.cross_val_score
- sklearn.model_selection.cross_validate
- 模型稳定性评估

难度：⭐⭐⭐
"""

import numpy as np

# TODO: 1. 用注释解释交叉验证的原理和优势
# 为什么比单次划分训练集/测试集更好？
# 在此处写注释


# TODO: 2. 使用 5 折交叉验证评估决策树模型
# 加载数据集，使用 cross_val_score, cv=5
# 打印每次折叠的得分
# 在此处写代码


# TODO: 3. 比较不同模型的交叉验证得分
# 决策树、随机森林、逻辑回归
# 在此处写代码


# TODO: 4. 使用 cross_validate 获取多个指标
# 同时评估 accuracy 和 recall
# 在此处写代码


# TODO: 5. 输出交叉验证的平均得分和标准差
# 使用 np.mean() 和 np.std()
# 在此处写代码
