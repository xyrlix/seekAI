# -*- coding: utf-8 -*-
# @file    : polygon2_256360245.py
# @brief   : 点类测试
# @author  : xyrlix (xyrlix@qq.com)
# @date    : 2025-11-17 11:07:07
# @copyright: Copyright (c) 2025 Seek Dao


from polygon import Point3D, Point

# 测试 Point3D 类
if __name__ == "__main__":
    stdid = '256360245'
    print(f"stdid: {stdid}")
    a = int(stdid[-1])
    b = int(stdid[-2])
    pt1 = Point(1, a)
    pt2 = Point(0, 0)
    pt3 = Point3D(1, 2, 0)
    pt4 = Point3D(-1, 0, b)
    gen_obj = (x for x in [pt1, pt2, pt3, pt4])
    print(f'{"".join([str(y)+".-." for y in gen_obj])}')
