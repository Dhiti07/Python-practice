class Graph:
    def __init__(self):
        self.graph = {}  
        self.nodes = []  
    def add_edge(self, u, v, weight=1):
        if u not in self.graph:
            self.graph[u] = []
            self.nodes.append(u)
        if v not in self.graph:
            self.graph[v] = []
            self.nodes.append(v)
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))
    def print_adjacency_list(self):
        print("Adjacency List:")
        for node in self.graph:
            neighbors = [f"{neighbor}" for neighbor, _ in self.graph[node]]
            print(f"{node}: {neighbors}")
    def print_adjacency_matrix(self):
        size = len(self.nodes)
        index_map = {self.nodes[i]: i for i in range(size)}
        matrix = [[0] * size for _ in range(size)]
        for node in self.graph:
            for neighbor, weight in self.graph[node]:
                matrix[index_map[node]][index_map[neighbor]] = weight
        print("\nAdjacency Matrix:")
        for row in matrix:
            print(row)
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'E')
g.add_edge('A', 'C')
g.add_edge('B', 'C')
g.add_edge('C', 'D')
g.add_edge('C', 'E')
g.print_adjacency_list()
g.print_adjacency_matrix()
