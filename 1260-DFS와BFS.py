import sys 
from collections import deque

N, M, V = map(int, sys.stdin.readline().strip().split(' '))
graph = [[] for _ in range(N+1)]

if M == 0:
    print(V)
    print(V)
    sys.exit()

for _ in range(M) :
    x, y = map(int, sys.stdin.readline().strip().split(' '))
    graph[x].append(y)
    graph[y].append(x)

for i in range(N+1) :
    graph[i].sort()

if len(graph[V]) == 0 :
    print(V)
    print(V)
    sys.exit()

def DFS(graph, start, visited=[]) :
    visited.append(start)
    for node in graph[start] : 
        if node not in visited :
            DFS(graph, node, visited)
    return visited

def BFS(graph, start, visited=[]) :
    queue = deque([start])
    visited.append(start)

    while queue :
        v = queue.popleft()
        for i in graph[v] :
            if i not in visited: 
                queue.append(i)
                visited.append(i)
    return visited
            
result1 = DFS(graph, V)
result2 = BFS(graph, V)

for i in result1 :
    print(i, end= ' ')
print()
for i in result2 :
    print(i, end= ' ')