#to detect if there are any cycles or not
def has_cycle(graph, node, visited, rec_stack):
    visited.add(node)
    rec_stack.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited and has_cycle(graph, neighbor, visited, rec_stack):
            return True
        elif neighbor in rec_stack:  
            return True
    rec_stack.remove(node)
    return False
def detect_cycle(graph):
    visited = set()
    rec_stack = set()
    for node in graph:
        if node not in visited:
            if has_cycle(graph, node, visited, rec_stack):
                return True
    return False
graph = {
    0: [1], 
    1: [], 
    2: [0, 3], 
    3: [2, 3] 
}
print("Cycle detected:" if detect_cycle(graph) else "No cycle detected")
