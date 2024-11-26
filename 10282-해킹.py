import sys
input = sys.stdin.readline
import heapq

T = int(input().rstrip())
INF = 10e9

# 시작 노드에서 모든 노드들 까지 최단거리 구하기
def dijkstra(start, distance):
        # 초기 세팅
        distance[start] = 0
        q = []
        heapq.heappush(q, (0,start))
        
        while q:
            time, computer = heapq.heappop(q)

            # 해당 노드로 가는거 계산하기도 전에 거리가 길면 패스
            if distance[computer] < time : continue

            # 경유와 직행 중 최단거리로 최신화
            for nc, t in graph[computer]:
                # 경유하는것이 더 최단 거리일 경우에만 탐색
                if t + time < distance[nc]:
                    distance[nc] =  time+t
                    heapq.heappush(q, (distance[nc], nc))

for _ in range(T):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append([a,s])

    distance = [INF]*(n+1)

    dijkstra(c, distance)

    max_time = 0
    for i in distance:
        if i == INF: continue
        max_time = max(max_time, i)
    
    print(n - distance.count(INF) + 1, max_time)

