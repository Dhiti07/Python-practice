class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def display_graph(self):
        for node in self.graph:
            for neighbor in self.graph[node]:
                print(f"({node} ⟶ {neighbor})", end=" ")
            print()
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 1)
g.add_edge(3, 2)
g.add_edge(4, 5)
g.add_edge(5, 4)
g.display_graph()
