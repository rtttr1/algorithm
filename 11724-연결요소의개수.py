import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split(" "))
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N)]

for _ in range(M) :
    u, v = map(int, sys.stdin.readline().strip().split(" "))
    graph[u].append(v)
    graph[v].append(u)

def BFS(start):
    queue = deque([*graph[start]])
    check = [start]
    visited[start-1] = True

    while queue :
        node = queue.popleft()
        visited[node-1] = True

        if node not in check :
            check.append(node)
            for elem in graph[node] :
                queue.append(elem)
    return check

count = 0
for i in range(N) :
    if not visited[i] :
        BFS(i+1) 
        count += 1

print(count)