"""
任务 36：特征重要性分析

任务要求：
1. 使用 sklearn 内置数据集（如乳腺癌数据集或波士顿房价）
2. 分别使用决策树和随机森林训练模型
3. 提取并可视化各特征的重要性
4. 找出最重要的 3 个特征
5. 分析特征重要性与实际业务的关系

知识点：
- 特征重要性概念
- DecisionTreeClassifier.feature_importances_
- RandomForestClassifier.feature_importances_
- matplotlib 可视化

难度：⭐⭐⭐
"""

import numpy as np
import matplotlib.pyplot as plt

# TODO: 1. 加载数据集
# 使用 sklearn.datasets.load_breast_cancer() 或 load_wine()
# 打印数据集的特征名称
# 在此处写代码


# TODO: 2. 训练决策树模型
# 使用 DecisionTreeClassifier, random_state=42
# 在此处写代码


# TODO: 3. 训练随机森林模型
# 使用 RandomForestClassifier, n_estimators=100, random_state=42
# 在此处写代码


# TODO: 4. 提取并可视化特征重要性
# - 使用柱状图展示
# - 横轴：特征名称，纵轴：重要性分数
# 在此处写代码


# TODO: 5. 输出最重要的 3 个特征名称及其分数
# 使用 np.argsort 排序
# 在此处写代码
