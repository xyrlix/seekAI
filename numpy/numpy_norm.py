# -*- coding: utf-8 -*-
# @file    : numpy_norm.py
# @brief   : 求范数 norm
# @author  : xyrlix (xyrlix@outlook.com)
# @date    : 2025-10-16 03:30:02
# @copyright: Copyright (c) 2025 Seek Dao

import numpy as np

# 定义一个向量
v = np.array([3, 4])

# 计算 L2 范数 (默认)
l2_norm = np.linalg.norm(v)
# 或者明确指定 ord=2
l2_norm_explicit = np.linalg.norm(v, ord=2)

# 计算 L1 范数
l1_norm = np.linalg.norm(v, ord=1)

# 计算 L∞ 范数
l_inf_norm = np.linalg.norm(v, ord=np.inf)

print("--- 向量范数 ---")
print(f"向量 v: {v}")
print(f"L2 范数 (几何长度): {l2_norm}")       # 结果: 5.0 (因为 √(3²+4²) = √25 = 5)
print(f"L1 范数 (绝对值之和): {l1_norm}")      # 结果: 7.0 (因为 3+4=7)
print(f"L∞ 范数 (最大绝对值): {l_inf_norm}")   # 结果: 4.0 (因为 max(3,4)=4)


# 定义一个矩阵
A = np.array([[1, 2],
              [3, 4]])

# 计算 Frobenius 范数 (默认)
fro_norm = np.linalg.norm(A)
# 或者明确指定 ord='fro'
fro_norm_explicit = np.linalg.norm(A, ord='fro')

# 计算最大列和范数 (ord=1)
col_sum_norm = np.linalg.norm(A, ord=1)

# 计算最大行和范数 (ord=np.inf)
row_sum_norm = np.linalg.norm(A, ord=np.inf)

print("\n--- 矩阵范数 ---")
print(f"矩阵 A:\n{A}")
print(f"Frobenius 范数: {fro_norm}")          # 结果: √(1²+2²+3²+4²) = √30 ≈ 5.477
print(f"最大列和范数 (ord=1): {col_sum_norm}")  # 结果: max(1+3, 2+4) = max(4, 6) = 6
print(f"最大行和范数 (ord=inf): {row_sum_norm}") # 结果: max(1+2, 3+4) = max(3, 7) = 7


# 定义一个 3x2 的矩阵
B = np.array([[1, 2],
              [3, 4],
              [5, 6]])

# 计算每一列的 L2 范数 (axis=0)
col_norms = np.linalg.norm(B, axis=0)

# 计算每一行的 L2 范数 (axis=1)
row_norms = np.linalg.norm(B, axis=1)

print("\n--- 沿轴计算范数 ---")
print(f"矩阵 B:\n{B}")
print(f"每一列的 L2 范数: {col_norms}") # 结果: [√(1²+3²+5²), √(2²+4²+6²)] = [√35, √56]
print(f"每一行的 L2 范数: {row_norms}") # 结果: [√(1²+2²), √(3²+4²), √(5²+6²)] = [√5, 5, √61]