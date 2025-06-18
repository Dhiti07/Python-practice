class Graph:
    def __init__(self, vertices):
        self.V = vertices  
        self.graph = [[] for _ in range(vertices)]  
    def add_edge(self, u, v):
        self.graph[u].append(v)
    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=" ")  
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)
    def dfs(self, start_vertex):
        visited = [False] * self.V
        self.dfs_util(start_vertex, visited)
g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)
print("DFS Traversal starting from vertex 5:")
g.dfs(5)
