class Graph:
    def __init__(self):
        self.graph = {}  

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))  # Store destination node with weight

    def display_graph(self):
        for node in self.graph:
            for neighbor, weight in self.graph[node]:
                print(f"({node} ⟶ {neighbor}, {weight})")
g = Graph()
g.add_edge(0, 1, 6)
g.add_edge(1, 2, 7)
g.add_edge(2, 0, 5)
g.add_edge(2, 1, 4)
g.add_edge(3, 2, 10)
g.add_edge(4, 5, 1)
g.add_edge(5, 4, 3)
g.display_graph()
