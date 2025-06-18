from queue import PriorityQueue
graph = {
    'A':[('B',6),('F',3)],'B':[('A',6),('D',2),('C',3)],'C':[('D',1),('B',3),('E',5)],
    'D':[('B',2),('C',1),('E',9),('G',5)],'E':[('D',8),('C',5),('I',5),('J',5)],
    'J':[('E',5),('I',3)],
    'I':[('E',5),('J',3),('G',3),('H',2)],
    'G':[('I',3),('F',1),('D',5)],
    'F':[('G',1),('H',7),('A',3)],
    'H':[('F',7),('I',2)]
}
heuristic = {
    'A':10,'B':8,'C':5,'D':7,'E':3,'F':6,'G':5,'H':3,'I':1
}
def astar(start,goal):
    pq = PriorityQueue()
    pq.put((0+heuristic[start], 0,start,[start]))
    visited = set()
    while not pq.empty:
        f,cost,node,path = pq.get()
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                total_cost = cost +weight
                pq.put((total_cost+heuristic[neighbor],total_cost,neighbor,path+[neighbor]))
print(astar('A','J'))