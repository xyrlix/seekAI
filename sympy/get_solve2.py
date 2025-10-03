# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 12:29:23 2025

@author: xyrlix
"""

from sympy import *

"""
求解下面问题：
1.给定函数 f(x)=x^3−3^2+2,求解方程f(x)=0的根。
2.给定函数 f(x)=x^3−3^2+2,解方程f’(x)=0,并带入原函数求极值。
"""


x = symbols('x')
f = x**3 - 3*x**2 + 2

# 得到方程：
print('方程 f(x) = ', f)

""" 任务1：求解方程 f(x) = 0 的根 """
print("方程 f(x)=0 的根：", solve(f, x))


""" 任务2：求解 f'(x)=0 并求极值 """
df = diff(f, x)
print('求解 f\'(x)=0 , 得到：', solve(df, x))

print('求解 f\'(x) > 0 , 递增区间：', solve(df > 0, x))
print('求解 f\'(x) < 0 , 递减区间：', solve(df < 0, x))

# 求极值
extremes = [(point, f.subs(x, point)) for point in solve(df, x)]
max_value = extremes[0][0]
min_value = extremes[0][0]
for point, value in extremes:
    print(f"当 x = {point} 时，原函数的极值为 {value}")
    if value > max_value:
            max_value = value
    if value < min_value:
            min_value = value
        
print('f(x) 极大值是：', max_value)
print('f(x) 极小值是：', min_value)