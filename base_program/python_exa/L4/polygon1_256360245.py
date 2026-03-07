# -*- coding: utf-8 -*-
# @file    : polygon1_256360245.py
# @brief   : 点类测试
# @author  : xyrlix (xyrlix@qq.com)
# @date    : 2025-11-17 11:07:07
# @copyright: Copyright (c) 2025 Seek Dao

from polygon import Point

# 测试 Point 类
if __name__ == "__main__":
    print(Point.__doc__)
    stdid = '256360245'
    a = int(stdid[-1])
    pt1 = Point(1, a)
    pt2 = Point(0, 0)
    print(type(iter(pt1)))
    print(f"{pt1}-{pt2}")
    for element in pt1:
        print(f"<{element}>")
