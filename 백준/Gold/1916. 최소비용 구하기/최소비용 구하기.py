import sys
input = sys.stdin.readline
import heapq

N = int(input().rstrip())
M = int(input().rstrip())
INF = 1e9

graph = [[] for _ in range(N+1)]
distance = [INF]*(N+1)

for _ in range(M):
    u, v, cost = map(int, input().split())
    graph[u].append([v, cost])

start, end = map(int, input().split())

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        cost, now = heapq.heappop(q)

        if distance[now] < cost: continue 

        for v, c in graph[now]:
            if distance[v] > c + distance[now]:
                distance[v] = c + distance[now]
                heapq.heappush(q, (c + distance[now], v))

dijkstra(start)
    
print(distance[end])