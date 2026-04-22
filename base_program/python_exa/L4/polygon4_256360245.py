# -*- coding: utf-8 -*-
# @file    : polygon4_256360245.py
# @brief   : 多边形类测试
# @author  : xyrlix (xyrlix@qq.com)
# @date    : 2025-11-17 11:07:07
# @copyright: Copyright (c) 2025 Seek Dao


import matplotlib.pyplot as plt
import numpy as np
from polygon import Point3D, Triangle, Quadrilateral

if __name__ == "__main__":
    stdid = '256360245'
    a = int(stdid[-1])
    b = int(stdid[-2])
    c = int(stdid[-3])
    pt1 = Point3D(0, 0, 0)
    pt2 = Point3D(0, 1, a)
    pt3 = Point3D(-5, 2, b)
    pt4 = Point3D(-3, 0, c)
    
    print(f"stdid: {stdid}")
    tri1 = Triangle([pt2, pt3, pt4])
    print("---"*20)
    print(tri1)
    print(f"sides_length: {tri1.sides_length()}")
    print(f"Area: {tri1.area()}")
    
    quad1 = Quadrilateral([pt1, pt2, pt3, pt4])
    print("---"*20)
    print(quad1)
    print(f"sides_length: {quad1.sides_length()}")
    print(f"Area: {quad1.area()}")
    
    # 可选：3D绘图展示
    plt.style.use('_mpl-gallery')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10), subplot_kw={"projection": "3d"})

    # 三角形绘图
    tri_xs = np.array([p.point[0] for p in tri1.points] + [tri1.points[0].point[0]])
    tri_ys = np.array([p.point[1] for p in tri1.points] + [tri1.points[0].point[1]])
    tri_zs = np.array([p.point[2] for p in tri1.points] + [tri1.points[0].point[2]])
    ax1.plot(tri_xs, tri_ys, tri_zs, 'r-', markersize=8)
    ax1.scatter(tri_xs[:-1], tri_ys[:-1], tri_zs[:-1], c='blue', s=50)
    ax1.set_title('Triangle Visualization', fontsize=14, pad=20)

    # 四边形绘图
    quad_xs = np.array([p.point[0] for p in quad1.points] + [quad1.points[0].point[0]])
    quad_ys = np.array([p.point[1] for p in quad1.points] + [quad1.points[0].point[1]])
    quad_zs = np.array([p.point[2] for p in quad1.points] + [quad1.points[0].point[2]])
    ax2.plot(quad_xs, quad_ys, quad_zs, 'g-', markersize=8)
    ax2.scatter(quad_xs[:-1], quad_ys[:-1], quad_zs[:-1], c='red', s=50)
    ax2.set_title('Quadrilateral Visualization', fontsize=14, pad=20)

    plt.subplots_adjust(top=0.9)
    plt.tight_layout()
    plt.show()
