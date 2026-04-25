"""
任务 21：pandas 统计分析

任务要求：
1. 基本统计（均值、中位数、标准差）
2. 分组统计（groupby）
3. 排序
4. 数据透视表（pivot_table）
5. 合并多个 DataFrame

知识点：
- df.mean(), df.median(), df.std()
- df.groupby()
- df.sort_values()
- pd.pivot_table()
- pd.merge()

难度：⭐⭐⭐
"""
import pandas as pd

# 创建学生成绩数据
data = {
    "name": ["小明", "小红", "小刚", "小李", "小华", "小王"],
    "class": ["A", "B", "A", "B", "A", "B"],
    "math": [95, 88, 92, 85, 90, 78],
    "english": [85, 92, 88, 95, 80, 85],
    "python": [90, 85, 95, 88, 92, 80]
}
df = pd.DataFrame(data)

# TODO: 1. 计算每门课程的均值、中位数、标准差



# TODO: 2. 使用 groupby 按班级分组，计算每班平均分



# TODO: 3. 按数学成绩降序排序



# TODO: 4. 创建数据透视表：行是班级，列是科目，值是平均分



# TODO: 5. 创建第二个 DataFrame（学生年龄），合并到原数据
# ages = {"name": [...], "age": [...]}
