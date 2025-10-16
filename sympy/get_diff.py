# -*- coding: utf-8 -*-
# @file    : get_diff.py
# @brief   : 求导数diff
# @author  : xyrlix (xyrlix@outlook.com)
# @date    : 2025-10-03 01:45:47
# @copyright: Copyright (c) 2025 Seek Dao


# 用符号计算库 sympy


# 求解函数的导数 diff


from sympy import *

x, y = symbols('x, y')
f = 5*x**3*y**3 - 8*y
print('f =', f)
fx = diff(f, x)
print('fx =', fx)
fy = diff(f, y)
print('fy =', fy)