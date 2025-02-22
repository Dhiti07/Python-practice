def bfs_tsp(graph, start):
    queue = [(start, [start], 0)] 
    min_path, min_cost = None, float('inf')
    while queue:
        node, path, cost = queue.pop(0)  
        if len(path) == len(graph) and path[0] in graph[node]: 
            cost += graph[node][path[0]]
            if cost < min_cost:
                min_cost = cost
                min_path = path + [path[0]]
        for neighbor in graph[node]:
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor], cost + graph[node][neighbor]))
    return min_path, min_cost
graph = {
    'A': {'B': 2, 'C': 3, 'D': 1},
    'B': {'A': 2, 'C': 4, 'D': 2},
    'C': {'A': 3, 'B': 4, 'D': 3},
    'D': {'A': 1, 'B': 2, 'C': 3}
}
start_node = 'A'
path, cost = bfs_tsp(graph, start_node)
print("Shortest TSP Path:", path)
print("Minimum Cost:", cost)
