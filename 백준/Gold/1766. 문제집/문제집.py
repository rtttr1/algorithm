import sys
from queue import PriorityQueue

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    queue = PriorityQueue()

    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.put(i)
    
    while not queue.empty():
        now = queue.get()
        result.append(now)
  
        for edge in graph[now]:
            indegree[edge] -= 1
            if indegree[edge] == 0:
                queue.put(edge)
    
    for res in result:
        print(res, end = ' ')

topology_sort()
