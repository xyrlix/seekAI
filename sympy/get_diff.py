# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 10:16:13 2025

@author: uding
"""


# 求解函数的导数 diff


from sympy import *

x, y = symbols('x, y')
f = 5*x**3*y**3 - 8*y
print('f =', f)
fx = diff(f, x)
print('fx =', fx)
fy = diff(f, y)
print('fy =', fy)