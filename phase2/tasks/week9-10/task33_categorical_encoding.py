"""
任务 33：类别特征编码

任务要求：
1. 创建包含类别特征的数据集（如：城市、颜色、学历）
2. 使用 LabelEncoder 进行标签编码
3. 使用 OneHotEncoder 进行独热编码
4. 比较两种编码方式的输出
5. 解释各自适用场景

知识点：
- 类别特征编码概念
- sklearn.preprocessing.LabelEncoder
- sklearn.preprocessing.OneHotEncoder

难度：⭐⭐
"""

import numpy as np

# TODO: 1. 创建包含类别特征的数据
# 示例：城市 = ['北京', '上海', '广州', '北京', '上海']
# 示例：学历 = ['本科', '硕士', '博士', '本科', '硕士']
# 在此处写代码


# TODO: 2. 使用 LabelEncoder 对城市进行编码
# 打印原始数据和编码结果
# 在此处写代码


# TODO: 3. 使用 OneHotEncoder 对学历进行独热编码
# 需要调整数据形状（使用 reshape）
# 打印编码结果
# 在此处写代码


# TODO: 4. 尝试反转编码
# 使用 inverse_transform() 还原原始数据
# 在此处写代码


# TODO: 5. 用注释解释两种编码的适用场景
# LabelEncoder 适用于：
# OneHotEncoder 适用于：
