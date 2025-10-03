# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 10:16:13 2025

@author: uding
"""


# 求解函数的极值sovle


from sympy import *


# 求解 x^2 - 3x + 2 = 0 与 x^2 - 3x + 2 > 0
print('求解 x^2 - 3x + 2 = 0 与 x^2 - 3x + 2 > 0')
x = symbols('x')
f = x**2 - 3 *x + 2

print('f = ', f)
print('f = 0 的解：', solve(f, x))
print('f > 0 的解：', solve(f>0, x))
print('=====================\n')

# 求解 :
# 4x - 3y = 5
# 3x + 2y = 8
print("求解 : \n\t4x - 3y = 5\n\t3x + 2y = 8")
x, y = symbols('x, y')
f1 = 4*x - 3 *y - 5
f2 = 3 *x + 2 *y - 8
print(solve([f1, f2], [x, y]))
print('=====================\n')


print('求解：x^3 - 3x^2 -9x + 5的极值')
f = x**3 - 3 *x ** 2 - 9 * x + 5
df = diff(f, x)
print("驻点：", solve(df, x))
print("单调增区间:", solve(df > 0, x))
print("单调减区间:", solve(df < 0, x))
print('=====================\n')


# 设函数 f(x, y, z) = x^2 + 7y + z, 求f(2, 4, 1)
print('设函数 f(x, y, z) = x^2 + 7y + z, 求f(2, 4, 1)')
x, y, z = symbols('x, y, z')
f = x**2 +7*y + z
print('f(x, y, z) =', f)
print('f(2, 4, 1) = ', f.subs([(x, 2), (y, 4), (z ,1)]))