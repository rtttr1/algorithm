import sys
input = sys.stdin.readline
import heapq
INF = 1e8
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())

    graph[a].append([b,c])
    graph[b].append([a,c])

distance = [INF]*(N+1)

def dijkstra():
    queue = []
    heapq.heappush(queue, [1, 0])

    while queue:
        node, weight = heapq.heappop(queue)

        if distance[node] < weight:
            continue

        for i in graph[node]:
            if weight+i[1] < distance[i[0]]:
                distance[i[0]] = weight + i[1]
                heapq.heappush(queue, [i[0], weight+i[1]])

dijkstra()
print(distance[-1])