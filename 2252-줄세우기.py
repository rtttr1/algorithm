import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    queue = deque([])
    result = []

    for i in range(1, N+1):
        if indegree[i] == 0: queue.append(i)

    while queue:
        now = queue.popleft()
        result.append(now)

        for node in graph[now]:
            indegree[node] -= 1
            if indegree[node] == 0: 
                queue.append(node)
        
    return result

result = topology_sort()

print(' '.join(map(str, result)))
