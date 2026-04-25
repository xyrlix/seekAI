"""
任务 17-24 参考答案 - Week 5-6
numpy、pandas、matplotlib、AI 概念
"""
import numpy as np

# ==================== 任务 17：numpy 数组基础 ====================
print("=" * 40)
print("任务 17：numpy 数组基础")
print("=" * 40)

# 1. 创建数组
arr1d = np.array([1, 2, 3, 4, 5])
arr2d = np.array([[1, 2], [3, 4]])
print(f"一维数组：{arr1d}")
print(f"二维数组：\n{arr2d}")

# 2. 索引和切片
print(f"第一个元素：{arr1d[0]}")
print(f"前两行：\n{arr2d[:2]}")

# 3. reshape
reshaped = arr1d.reshape(5, 1)
print(f"reshape (5,1)：\n{reshaped}")

# 4. 数组运算
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(f"a + b = {a + b}")
print(f"a * b = {a * b}")

# 5. 特殊数组
print(f"全0数组：\n{np.zeros((3, 3))}")
print(f"随机数组：\n{np.random.rand(3)}")
print(f"等差数列：{np.arange(0, 11, 2)}")


# ==================== 任务 18：numpy 矩阵运算 ====================
print("\n" + "=" * 40)
print("任务 18：numpy 矩阵运算")
print("=" * 40)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# 点积
print(f"矩阵点积：\n{np.matmul(A, B)}")

# 转置
print(f"A 的转置：\n{A.T}")

# 统计
data = np.array([1, 2, 3, 4, 5])
print(f"均值：{data.mean()}")
print(f"标准差：{data.std()}")
print(f"最大值：{data.max()}")
print(f"最小值：{data.min()}")


# ==================== 任务 19-21：pandas ====================
print("\n" + "=" * 40)
print("任务 19-21：pandas 数据处理")
print("=" * 40)

import pandas as pd

# 创建 DataFrame
data = {
    "name": ["小明", "小红", "小刚", "小李", "小华"],
    "class": ["A", "B", "A", "B", "A"],
    "math": [95, 88, 92, 85, 90],
    "english": [85, 92, 88, 95, 80],
    "python": [90, 85, 95, 88, 92]
}
df = pd.DataFrame(data)

print("原始数据：")
print(df)

# 基本信息
print(f"\n基本信息：")
print(df.info())

# 统计
print("\n统计信息：")
print(df[["math", "english", "python"]].describe())

# 按班级分组
print("\n班级平均分：")
print(df.groupby("class")[["math", "english", "python"]].mean())

# 排序
print("\n按数学成绩排序：")
print(df.sort_values("math", ascending=False))

# 筛选
print("\n数学成绩>90的学生：")
print(df[df["math"] > 90])


# ==================== 任务 22：matplotlib ====================
print("\n" + "=" * 40)
print("任务 22：matplotlib 可视化")
print("=" * 40)

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 简单折线图示例
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, label='sin(x)')
plt.title('正弦函数')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('phase1/answers/week5-6/sin_plot.png', dpi=100)
plt.close()
print("图表已保存到 sin_plot.png")


# ==================== 任务 23：AI 概念学习 ====================
print("\n" + "=" * 40)
print("任务 23：AI 核心概念笔记")
print("=" * 40)

ai_notes = """
AI 核心概念总结：

1. AI (人工智能)：让机器模拟人类智能
2. ML (机器学习)：从数据中学习规律
3. DL (深度学习)：多层神经网络的 ML

关系：AI ⊃ ML ⊃ DL

开发流程：
数据收集 → 预处理 → 模型选择 → 训练 → 评估 → 部署 → 优化

关键术语：
- 模型：从数据中学到的规则
- 训练：让模型学习的过程
- 推理：用模型预测新数据
- 损失函数：衡量预测与真实值的差距
- 过拟合：模型记住了训练数据
"""
print(ai_notes)


# ==================== 任务 24：综合项目 ====================
print("\n" + "=" * 40)
print("任务 24：数据分析综合项目")
print("=" * 40)

# 创建模拟数据
np.random.seed(42)
n_students = 30
student_data = {
    "name": [f"学生{i+1}" for i in range(n_students)],
    "class": np.random.choice(["A班", "B班"], n_students),
    "math": np.random.randint(50, 100, n_students).astype(float),
    "english": np.random.randint(50, 100, n_students).astype(float),
    "python": np.random.randint(50, 100, n_students).astype(float)
}

# 添加缺失值和异常值
student_data["math"][2] = np.nan
student_data["english"][5] = -10
student_data["python"][8] = 105

df_raw = pd.DataFrame(student_data)
print(f"原始数据 ({len(df_raw)} 行)：")
print(df_raw.head())

# 数据清洗
df_clean = df_raw.copy()
df_clean = df_clean.replace(-10, np.nan)
df_clean.loc[df_clean["python"] > 100, "python"] = np.nan

for col in ["math", "english", "python"]:
    df_clean[col] = df_clean[col].fillna(df_clean[col].median())

print(f"\n清洗后数据：")
print(df_clean.head())

# 统计分析
print(f"\n各科平均分：")
print(df_clean[["math", "english", "python"]].mean())

print(f"\n班级对比：")
print(df_clean.groupby("class")[["math", "english", "python"]].mean())

print(f"\n最高分学生：")
for subject in ["math", "english", "python"]:
    idx = df_clean[subject].idxmax()
    print(f"  {subject}: {df_clean.loc[idx, 'name']} ({df_clean.loc[idx, subject]}分)")

# 可视化
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# 各科平均分柱状图
subjects = ["math", "english", "python"]
means = df_clean[subjects].mean()
axes[0].bar(subjects, means.values)
axes[0].set_title("各科平均分")
axes[0].set_ylabel("分数")

# 班级对比
class_means = df_clean.groupby("class")[subjects].mean()
class_means.plot(kind="bar", ax=axes[1])
axes[1].set_title("班级成绩对比")
axes[1].set_ylabel("平均分")

plt.tight_layout()
plt.savefig('phase1/answers/week5-6/final_analysis.png', dpi=100)
plt.close()
print("\n分析图表已保存到 final_analysis.png")

# 生成报告
report = f"""
数据分析报告
==============
学生总数：{len(df_clean)}
班级数量：{df_clean['class'].nunique()}

各科平均分：
{means.to_string()}

班级平均分对比：
{class_means.to_string()}
"""
print(report)
