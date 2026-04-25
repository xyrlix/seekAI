"""
任务 20：pandas 数据清洗

任务要求：
1. 创建包含缺失值的数据
2. 删除缺失值（dropna）
3. 填充缺失值（fillna）
4. 替换特定值
5. 去除重复行

知识点：
- df.dropna()
- df.fillna()
- df.replace()
- df.drop_duplicates()

难度：⭐⭐⭐
"""
import pandas as pd
import numpy as np

# 创建包含缺失值和重复行的数据
data = {
    "name": ["小明", "小红", "小刚", None, "小明", "小李"],
    "age": [20, 21, None, 22, 20, 19],
    "score": [95, np.nan, 88, 92, 95, 78]
}
df = pd.DataFrame(data)

# TODO: 1. 打印原始数据，查看缺失值



# TODO: 2. 使用 dropna() 删除包含缺失值的行



# TODO: 3. 使用 fillna() 填充缺失值（年龄用均值，成绩用中位数）



# TODO: 4. 将成绩中的负数替换为 0（假设负数是错误数据）



# TODO: 5. 删除重复行



# TODO: 6. 综合清洗：对数据进行完整的清洗流程
