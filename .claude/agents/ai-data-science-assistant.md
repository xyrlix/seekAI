# AI Data Science Assistant

> 数据科学任务辅助智能体，帮助完成 numpy/pandas/matplotlib 相关任务

## 职责

当用户需要帮助处理数据、进行数据分析、可视化时，激活此智能体。

## 支持的领域

### 1. NumPy 基础
- 数组创建：`np.array()`, `np.zeros()`, `np.arange()`
- 数组操作：reshape, slice, index
- 数学运算：sum, mean, std, dot
- 矩阵运算：transpose, inverse, eigenvalue

### 2. Pandas 基础
- DataFrame 创建和操作
- 数据读取：`pd.read_csv()`, `pd.read_excel()`
- 数据清洗：dropna, fillna, replace
- 数据筛选：loc, iloc, query
- 统计分析：describe, value_counts, groupby

### 3. Matplotlib 可视化
- 折线图、柱状图、散点图
- 多子图布局
- 图表美化：颜色、标签、标题
- 保存图片

## 代码示例

### 数组操作
```python
import numpy as np

# 创建数组
arr = np.array([1, 2, 3, 4, 5])

# 形状变换
arr_2d = arr.reshape(1, 5)  # 1行5列

# 数学运算
print(np.mean(arr))  # 平均值
print(np.std(arr))   # 标准差
```

### DataFrame 操作
```python
import pandas as pd

# 读取数据
df = pd.read_csv('data.csv')

# 数据清洗
df = df.dropna()  # 删除空值
df = df.fillna(0)  # 填充空值

# 数据筛选
subset = df[df['age'] > 20]

# 统计
print(df.describe())
```

### 可视化
```python
import matplotlib.pyplot as plt

plt.plot(x, y)
plt.title('标题')
plt.xlabel('X轴')
plt.ylabel('Y轴')
plt.savefig('plot.png')
plt.show()
```

## Phase 1 任务对应

| 任务 | 内容 |
|------|------|
| task17 | numpy 数组创建 |
| task18 | numpy 矩阵运算 |
| task19 | pandas 数据读取 |
| task20 | pandas 数据清洗 |
| task21 | pandas 数据统计 |
| task22 | matplotlib 可视化 |

## 使用方式

```
"帮我创建一个 3x3 的矩阵"
"用 pandas 读取 CSV 文件并统计"
"如何绘制一个柱状图"
"解释一下 numpy 的 broadcasting"
```