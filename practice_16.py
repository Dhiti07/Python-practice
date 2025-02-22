def topological_sort_bfs(vertices, edges):
    graph = {i: [] for i in vertices}
    in_degree = {i: 0 for i in vertices}
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    queue = [node for node in vertices if in_degree[node] == 0]
    order = []
    while queue:
        node = queue.pop(0) 
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return order
vertices = [0, 1, 2, 3, 4, 5]
edges = [(5, 0), (5, 2), (4, 0), (4, 1), (2, 3), (3, 1)]
print("Topological Order:", topological_sort_bfs(vertices, edges))
