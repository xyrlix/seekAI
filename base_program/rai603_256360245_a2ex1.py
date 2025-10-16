# -*- coding: utf-8 -*-
# @file    : rai603_256360245_a2ex1.py
# @brief   : a2ex1
# @author  : xyrlix (xyrlix@outlook.com)
# @date    : 2025-10-03 05:55:51
# @copyright: Copyright (c) 2025 Seek Dao


def fibonacci1(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end = ' ')
        a, b = b, a + b


def fibonacci2(n):
    if n <= 1:
        return n
    return fibonacci2(n - 1) + fibonacci2(n - 2)

print("fibinacci1 (for-loop):")
fibonacci1(20)

print("\nfibonacci2 (recursion):")
for k in range(20):
    print(fibonacci2(k), end=' ')