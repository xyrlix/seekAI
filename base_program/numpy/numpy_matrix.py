# -*- coding: utf-8 -*-
# @file    : numpy_matrix.py
# @brief   : numpy 矩阵
# @author  : xyrlix (xyrlix@qq.com)
# @date    : 2025-10-16 02:40:50
# @copyright: Copyright (c) 2025 Seek Dao

import numpy as np
import sympy as sp

A = np.array([[2, 1, -1, 2], [1, 3, -3, 4], [4, 2, -2, 4], [2, 1, -3, 5]])
print("矩阵A:\n", A)
rank = np.linalg.matrix_rank(A)
print("rank:", rank) # 求解矩阵的秩
A_matrix = sp.Matrix(A)
print("A_matrix:\n", A_matrix) # 将numpy矩阵转换为sympy矩阵
A_rref, out = A_matrix.rref() # 求解矩阵的行简化阶梯形
print("A_rref:\n", A_rref) # 求解矩阵的行简化阶梯形
print("out:\n", out) # 矩阵的秩
print("len(out):\n", len(out)) # 矩阵的秩