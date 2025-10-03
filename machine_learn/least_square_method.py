# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 14:58:49 2025

@author: xyrlix
"""


import numpy as np
import matplotlib as plt

# 1. 准备数据
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=np.float64)  # 天数
y = np.array([5, 7, 8, 11, 14, 13, 16, 18, 21, 22], dtype=np.float64)  # 销量
n = len(x)  # 数据点数量

# 2. 手动实现最小二乘法求解系数a和b
# 计算所需求和值
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x ** 2)

# 计算斜率a和截距b
a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
b = (sum_y - a * sum_x) / n

print("=" * 50)
print("1. 最小二乘法求解系数")
print(f"斜率 a = {a:.4f}")
print(f"截距 b = {b:.4f}")
print(f"线性回归模型：y = {a:.4f}x + {b:.4f}")
print("=" * 50)

# 3. 计算模型1（手动求解的模型）的MAE
y_pred1 = a * x + b  # 模型1的预测值
abs_error1 = np.abs(y - y_pred1)  # 绝对误差
mae1 = np.mean(abs_error1)  # 平均绝对误差

print("\n2. 模型1（y = {:.4f}x + {:.4f}）的MAE计算".format(a, b))
print("实际销量:", np.round(y, 2))
print("预测销量:", np.round(y_pred1, 4))
print("绝对误差:", np.round(abs_error1, 4))
print(f"MAE = {mae1:.4f}")
print("=" * 50)

# 4. 预测第12天的销量
x_12 = 12
y_pred_12 = a * x_12 + b
print(f"\n3. 第12天销量预测：{y_pred_12:.4f} 件")
print("=" * 50)

# 5. 计算模型2（y = 2.0x + 2.5）的MAE并对比
a2 = 2.0
b2 = 2.5
y_pred2 = a2 * x + b2  # 模型2的预测值
abs_error2 = np.abs(y - y_pred2)  # 模型2的绝对误差
mae2 = np.mean(abs_error2)  # 模型2的MAE

print("\n4. 模型对比")
print(f"模型2：y = {a2}x + {b2}")
print("模型2预测销量:", np.round(y_pred2, 2))
print("模型2绝对误差:", np.round(abs_error2, 2))
print(f"模型2 MAE = {mae2:.4f}")
print(f"\n模型1 MAE = {mae1:.4f}，模型2 MAE = {mae2:.4f}")
if mae1 < mae2:
    print("结论：模型1更优（MAE更小）")
else:
    print("结论：模型2更优（MAE更小）")
print("=" * 50)

# 6. 可视化拟合结果（可选）
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='实际销量数据')
plt.plot(x, y_pred1, color='red', label=f'模型1拟合线：y = {a:.4f}x + {b:.4f}')
plt.plot(x, y_pred2, color='green', linestyle='--', label=f'模型2拟合线：y = {a2}x + {b2}')
plt.scatter(x_12, y_pred_12, color='orange', s=100, label=f'第12天预测销量：{y_pred_12:.2f}件')
plt.xlabel('天数')
plt.ylabel('销量（件）')
plt.title('电商产品销量线性回归分析')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()