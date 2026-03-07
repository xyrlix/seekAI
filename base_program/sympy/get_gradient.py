# -*- coding: utf-8 -*-
# @file    : get_gradient.py
# @brief   : 求解下面问题：求梯度下降，得到x, y使得f(x, y) = x^2 + y^2最小
# @author  : xyrlix (xyrlix@qq.com)
# @date    : 2025-10-03 05:30:42
# @copyright: Copyright (c) 2025 Seek Dao

from sympy import *

max_iters = 1000
cur_x = 1
cur_y = 2

precision = 0.00001
learning_rate = 0.01

x, y = symbols('x, y')
f = x**2 + y**2

for i in range(max_iters):
    grad = [diff(f, x).subs(x, cur_x), diff(f, y).subs(y, cur_y)]
    print('grad:', grad)
    cur_x -= learning_rate * grad[0]
    cur_y -= learning_rate * grad[1]
    if abs(grad[0]) < precision and abs(grad[1]) < precision:
        break
print('最终结果：', cur_x, cur_y)