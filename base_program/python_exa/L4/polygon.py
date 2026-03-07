# -*- coding: utf-8 -*-
# @file    : polygon.py
# @brief   : 多边形类
# @author  : xyrlix (xyrlix@qq.com)
# @date    : 2025-11-17 11:07:07
# @copyright: Copyright (c) 2025 Seek Dao

from abc import ABC, abstractmethod
import math
import numpy as np


class Point:
    """class Point - Stores a point (x, y) in 2D space"""

    def __init__(self, x, y: int):
        self.point = [x, y]

    def __str__(self):
        return f"<{self.point}>"

    def gen(self):
        for c in self.point:
            yield c

    def __iter__(self):
        return self.gen()


class Point3D(Point):
    """class Point3D - Stores a point (x, y, z) in 3D space"""

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.point.append(z)


class Polygon():
    """Polygon base class - 接受定点坐标的点列表"""

    def __init__(self, points):
        self.points = points

    def __str__(self):
        return "Polygon: " + " -> ".join([str(pt) for pt in self.points])

    def __len__(self):
        return len(self.points)

    def gen(self):
        for c in self.points:
            yield c

    def __iter__(self):
        return self.gen()

    def _area_triangle(self, vec1: np.ndarray, vec2: np.ndarray) -> float:
        """内部方法：通过两个向量计算三角形面积"""
        cross_product = np.cross(vec1, vec2)
        return 0.5 * np.linalg.norm(cross_product)

    def sides_length(self):
        """计算多边形边长"""
        n = len(self.points)
        if n <= 1:
            return 0.0

        total_length = 0.0
        pts1 = self.points
        # 构造pts2：最后一个点连接回第一个点
        pts2 = self.points[1:] + [self.points[0]]

        # 遍历成对的点，计算距离并累加
        for p1, p2 in zip(pts1, pts2):
            # 确保两点维度一致（2D/3D）
            if len(p1.point) != len(p2.point):
                raise ValueError("Points must have the same dimension")
            total_length += math.dist(p1.point, p2.point)
        return round(total_length, 2)

    @abstractmethod
    def area(self):
        raise NotImplementedError("area() must be implemented")


class Triangle(Polygon):
    """class Triangle - 三角形"""

    def __init__(self, points: list[Point]):
        if len(points) != 3:
            raise ValueError("A triangle must have exactly 3 vertices")
        super().__init__(points)

    def __str__(self):
        return "Triangle: " + " -> ".join([str(pt) for pt in self.points])

    def area(self):
        """求三角形计算面积"""
        # 提取三点坐标并转换为向量
        p1 = np.array(self.points[0].point)
        p2 = np.array(self.points[1].point)
        p3 = np.array(self.points[2].point)

        # 计算向量
        vec1 = p2 - p1
        vec2 = p3 - p1

        # 计算面积
        return round(self._area_triangle(vec1, vec2), 2)


class Quadrilateral(Polygon):
    """class Quadrilateral - 四边形"""

    def __init__(self, points):
        if len(points) != 4:
            raise ValueError("A quadrilateral must have exactly 4 vertices")
        super().__init__(points)

    def __str__(self):
        return "Quadrilateral: " + " -> ".join([str(pt) for pt in self.points])

    def area(self):
        '''四边形计算面积'''
        # 提取四点坐标并转换为向量
        p1 = np.array(self.points[0].point)
        p2 = np.array(self.points[1].point)
        p3 = np.array(self.points[2].point)
        p4 = np.array(self.points[3].point)

        # 计算第一个三角形面积
        vec1 = p2 - p1
        vec2 = p4 - p1
        area1 = self._area_triangle(vec1, vec2)

        # 计算第二个三角形面积
        vec1 = p3 - p2
        vec2 = p4 - p2
        area2 = self._area_triangle(vec1, vec2)

        # 计算面积
        return abs(area1 + area2)
