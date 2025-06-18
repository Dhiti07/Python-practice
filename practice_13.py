def topological_sort_dfs(graph, node, visited, stack):
    visited.add(node)
    for neighbor in graph[node]:  
        if neighbor not in visited:
            topological_sort_dfs(graph, neighbor, visited, stack)
    stack.append(node)
def topological_sort(vertices, edges):
    graph = {node: [] for node in vertices}  
    for u, v in edges:
        graph[u].append(v)
    visited = set()
    stack = []
    for node in vertices:
        if node not in visited:
            topological_sort_dfs(graph, node, visited, stack)
    return stack[::-1]  
vertices = [0, 1, 2, 3, 4, 5]
edges = [(5, 0), (5, 2), (4, 0), (4, 1), (2, 3), (3, 1)]
result = topological_sort(vertices, edges)
print("Topological Sorting Order:", result)
