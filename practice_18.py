def ucs(graph, start, goal):
    queue, visited = [(0, start)], {}
    while queue:
        queue.sort()
        cost, node = queue.pop(0)
        if node in visited: continue
        visited[node] = cost
        if node == goal: return cost
        queue += [(cost + w, n) for n, w in graph.get(node, []) if n not in visited]
graph = {
    'S': [('1', 2), ('3', 5)],
    '1': [('G', 1)],
    '2': [('1', 4)],
    '3': [('G', 6), ('4', 2),('1',5)],
    '4': [('5', 3),('2',4)],
    '5': [('G', 3),('2',6)],
    'G': [('4',7)]
}
print("Minimum cost from S to G is =", ucs(graph, 'S', 'G'))
