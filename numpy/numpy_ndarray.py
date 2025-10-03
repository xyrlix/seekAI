# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 12:29:23 2025

@author: xyrlix
"""

import numpy as np

# 一维数组
a = np.array([1, 2, 3])
print(a)

# 二维数组
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print("维度：", b.shape)

# 调整维度
c = b.reshape(3, 2)
print(c)
print("维度：", c.shape)

# 创建数组
print("empty :", np.empty(3))
print("zeros:", np.zeros(3))
print("ones:", np.ones(3))
print("arange:", np.arange(3))

# 切片
a = np.arange(10)
print(a)
print(a[2:])
print(a[2:5])

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)
print(a[1:])

# 第二列
print(a[..., 1])
# 第二行
print(a[1, ...])
# 每行第二列开始所有
print(a[..., 1:])