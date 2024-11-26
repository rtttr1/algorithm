import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    p, c, v = map(int, input().split())
    graph[p].append([c,v])
    graph[c].append([p,v])

def bfs(start):
    distance = [-1]*(N+1)
    distance[start] = 0
    queue = deque([[start,0]])

    while queue:
        n,d = queue.popleft()

        for node, v in graph[n]:
            if distance[node] >= 0: continue
            queue.append([node,d+v])
            distance[node] = d+v
    return distance

d1 = bfs(1)
index = d1.index(max(d1))

print(max(bfs(index)))

