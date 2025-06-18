def dfs(capA, capB, goal):
    stack = [((0, 0), [])]
    visited = set()

    while stack:
        (a, b), path = stack.pop()
        if (a, b) in visited:
            continue
        visited.add((a, b))
        path = path + [(a, b)]

        if a == goal:
            return path

        next_states = set([
            (capA, b), (a, capB), (0, b), (a, 0),
            (min(a + b, capA), max(0, b - (capA - a))),
            (max(0, a - (capB - b)), min(a + b, capB))
        ])

        for state in next_states:
            stack.append((state, path))

    return None

path = dfs(4, 3, 2)
print(path)
