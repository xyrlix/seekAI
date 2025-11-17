from abc import abstractmethod
import math

class Point:
    """class Point - Stores a point (x, y) in 2D space"""
    def __init__(self, x, y:int):
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
        self.point = [x, y, z]
    def __str__(self):
        return f"<{self.point}>"
    def gen(self):
        for c in self.point:
            yield c
    def __iter__(self):
        return self.gen()

class Polygon:
    """Polygon base class - 接受定点坐标的点列表"""
    def __init__(self, points):
        self.points = points
    def __str__(self):
        return f"<{self.points}>"
    def __len__(self):
        return len(self.points)
    def gen(self):
        for c in self.points:
            yield c
    def __iter__(self):
        return self.gen()
    def sides_length(self):
        if len(self.points) <= 1:
            return 0
        if len(self.points) == 2:
            # 只有两个点
            pts1 = self.points[0]
            pts2 = self.points[1]
        else:
            # 多于两个点, 需要构造最后一条边
            pts1 = self.points
            pts2 = self.points[0:2]
        # 多边形边长 这两个列表中获取的同一位置的点定义
        # 并调用 math.dist() 函数计算总数至 total_length
        total_length = math.dist(pts1, pts2)
        return total_length
    @abstractmethod
    def area(self):
        raise NotImplementedError("area() must be implemented")

class Triangle(Polygon):
    """class Triangle - Stores a triangle in 3D space"""
    def __init__(self, points):
        super().__init__(points)
        self.edges = self.edges()
        self.area = self.area()
    def __str__(self):
        return f"<{self.points}>"
    def gen(self):
        for c in self.points:
            yield c
    def __iter__(self):
        return self.gen()

    def edges(self):
        return [self.points[0], self.points[1], self.points[2]]
    
    def area(self):
        '''三角形计算面积'''
        return 0.5 * abs(self.points[0].x * (self.points[1].y - self.points[2].y) + self.points[1].x * (self.points[2].y - self.points[0].y) + self.points[2].x * (self.points[0].y - self.points[1].y))

class Quadrilateral(Polygon):
    """class Quadrilateral - Stores a quadrilateral in 3D space"""
    def __init__(self, points):
        super().__init__(points)
        self.edges = self.edges()
        self.area = self.area()
    def __str__(self):
        return f"<{self.points}>"
    def gen(self):
        for c in self.points:
            yield c
    def __iter__(self):
        return self.gen()

    def edges(self):
        return [self.points[0], self.points[1], self.points[2], self.points[3]]
    
    def area(self):
        '''四边形计算面积'''
        return abs(self.points[0].x * (self.points[1].y - self.points[2].y) + self.points[1].x * (self.points[2].y - self.points[0].y) + self.points[2].x * (self.points[0].y - self.points[1].y)) / 2