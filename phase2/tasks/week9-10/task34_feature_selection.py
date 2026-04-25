"""
任务 34：特征选择

任务要求：
1. 创建包含多个特征的数据集（至少 5 个特征）
2. 使用 VarianceThreshold 删除低方差特征
3. 使用 SelectKBest 选择最优 K 个特征
4. 使用 RandomForest 计算特征重要性
5. 输出最终选择的最优特征列表

知识点：
- 特征选择的意义
- sklearn.feature_selection.VarianceThreshold
- sklearn.feature_selection.SelectKBest
- 特征重要性分析

难度：⭐⭐⭐
"""

import numpy as np

# TODO: 1. 创建数据集
# X: 100 个样本，5 个特征
# y: 二分类标签
# 其中 1-2 个特征为无用特征（如全为常数或随机噪声）
# 在此处写代码


# TODO: 2. 使用 VarianceThreshold 删除方差 < 0.1 的特征
# 打印选择后的特征数量
# 在此处写代码


# TODO: 3. 使用 SelectKBest 选择前 3 个最优特征
# 使用 f_classif 评分函数
# 打印各特征的得分
# 在此处写代码


# TODO: 4. 使用 RandomForestClassifier 计算特征重要性
# 打印各特征的重要性分数
# 在此处写代码


# TODO: 5. 综合以上方法，输出最终选择的最优特征索引
# 用注释解释选择理由
# 在此处写代码和注释
