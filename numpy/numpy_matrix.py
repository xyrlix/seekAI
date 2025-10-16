# -*- coding: utf-8 -*-
# @file    : numpy_matrix.py
# @brief   : 
# @author  : xyrlix (xyrlix@outlook.com)
# @date    : 2025-10-16 02:40:50
# @copyright: Copyright (c) 2025 Seek Dao

import numpy as np
import sympy as sp

A = np.array([[2, 1, -1, 2], [1, 3, -3, 4], [4, 2, -2, 4], [2, 1, -3, 5]])
print("A:\n", A)
rank = np.linalg.matrix_rank(A)
print("rank:", rank)
A_matrix = sp.Matrix(A)
print("A_matrix:\n", A_matrix)
A_rref, out = A_matrix.rref()
print("A_rref:\n", A_rref)
print("out:\n", out)
print("len(out):\n", len(out))