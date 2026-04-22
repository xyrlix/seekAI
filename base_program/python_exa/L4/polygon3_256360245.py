# -*- coding: utf-8 -*-
# @file    : polygon3_256360245.py
# @brief   : 多边形类测试
# @author  : xyrlix (xyrlix@qq.com)
# @date    : 2025-11-17 14:36:05
# @copyright: Copyright (c) 2025 Seek Dao


import matplotlib.pyplot as plt
import numpy as np
from polygon import Point3D, Polygon

if __name__ == "__main__":
    stdid = '256360245'
    a = int(stdid[-1])
    b = int(stdid[-2])
    c = int(stdid[-3])
    pt1 = Point3D(0, 0, 0)
    pt2 = Point3D(0, 1, a)
    pt3 = Point3D(-5, 2, b)
    pt4 = Point3D(-3, 0, c)
    poly1 = Polygon([pt1, pt2, pt3, pt4])
    print(f"stdid: {stdid}")
    print(poly1)
    print(f"sides_length: {poly1.sides_length()}")

    # Plot
    plt.style.use('_mpl-gallery')
    xs = np.array([pts.point[0] for pts in poly1.points])
    ys = np.array([pts.point[1] for pts in poly1.points])
    zs = np.array([pts.point[2] for pts in poly1.points])

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={"projection": "3d"})
    ax.plot(xs, ys, zs, 'b-', linewidth=2, markersize=8)
    ax.scatter(xs[:-1], ys[:-1], zs[:-1], c='red', s=50)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    # 设置标题，调整字体大小和位置
    ax.set_title(f'Polygon test: {stdid}', fontsize=14, pad=20)
    plt.subplots_adjust(top=0.9)
    plt.tight_layout()
    plt.show()
