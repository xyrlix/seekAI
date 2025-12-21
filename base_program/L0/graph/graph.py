from collections import deque

class Graph:
    def __init__(self, directed=False):
        self.graph = {}  # 使用字典存储图，键为顶点，值为其相邻的顶点列表
        self.directed = directed  # 是否是有向图

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            if not self.directed:  # 如果是无向图，则添加反方向的边
                self.graph[vertex2].append(vertex1)

    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")
    
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')
        for next_vertex in self.graph[start]:
            if next_vertex not in visited:
                self.dfs(next_vertex, visited)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


if __name__ == "__main__":
    g = Graph(directed=False)  # 创建一个无向图
    vertices = ['A', 'B', 'C', 'D', 'E']
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]

    # 添加顶点
    for v in vertices:
        g.add_vertex(v)

    # 添加边
    for e in edges:
        g.add_edge(e[0], e[1])

    print("邻接表表示的图:")
    g.print_graph()

    print("\n深度优先搜索(从顶点A开始):")
    g.dfs('A')

    print("\n\n广度优先搜索(从顶点A开始):")
    g.bfs('A')