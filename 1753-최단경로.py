import sys
import math
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input().rstrip())
graph = [[] for _ in range(V+1)]
distance = [math.inf]*(V+1)
visited = [False]*(V+1)

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)

        if visited[now]:
            continue

        for elem in graph[now]:
            if distance[elem[0]] > dist + elem[1]:
                distance[elem[0]] = dist + elem[1]
                heapq.heappush(q, (dist + elem[1], elem[0]))

        visited[now] = True

dijkstra(K)

for i in range(1, len(distance)):
    if distance[i] == math.inf:
        print("INF")
    else:
        print(distance[i])


