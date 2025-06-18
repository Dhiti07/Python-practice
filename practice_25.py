g = {'A': ['B', 'C'], 'B': ['D'], 'C': ['E'], 'D': [], 'E': []}
visited = set()
def dfs(n):
    if n not in visited:
        print(n)
        visited.add(n)
        for i in g[n]:
            dfs(i)
dfs('A')