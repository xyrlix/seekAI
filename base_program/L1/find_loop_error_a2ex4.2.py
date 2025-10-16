# -*- coding: utf-8 -*-
# @file    : a2ex4.2.py
# @brief   : a2ex4.2
# @author  : xyrlix (xyrlix@outlook.com)
# @date    : 2025-10-03 05:57:38
# @copyright: Copyright (c) 2025 Seek Dao

# 41
for j in range(26, 0, -1):
    print(j)
    
# 42
for i in range(1, 4):
    # print(i + " " + 2 ** i) # error
    print(str(i) + " " + str(2 ** i))
    
# 43
list1 = [2, 5, 7, 2, 7, 8]
list2 = []
for item in list1:
    if item not in list2:
        list2.append(item)
print(list2)

# 44
# error
list1 = ['a', 'b', 'c']
for letter in list1:
    letter = letter.upper()
print(list1)

# corret
list1 = ['a', 'b', 'c']
for i in range(len(list1)):
    list1[i] = list1[i].upper()  # 通过索引直接修改列表元素
print(list1)  # 输出: ['A', 'B', 'C']
