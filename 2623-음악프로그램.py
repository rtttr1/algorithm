import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)

for _ in range(M):
    arr = list(map(int, input().split()))

    for i in range(1, len(arr)-1):
        graph[arr[i]].append(arr[i+1])
        indegree[arr[i+1]] += 1



def topology_sort():
    result = []
    queue = deque([])

    for i in range(1, N+1): 
        if indegree[i] == 0: queue.append(i)
    
    while queue:
        now = queue.popleft()

        for node in graph[now]:
            indegree[node] -= 1
            if indegree[node] == 0: 
                queue.append(node)

        result.append(now)

    return result

result = topology_sort()

if len(result) != N: print(0)
else:
    for elem in result:
        print(elem)
    