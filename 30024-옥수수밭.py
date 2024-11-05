import sys
input = sys.stdin.readline
from queue import PriorityQueue

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
K = int(input().rstrip())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[False]*M for _ in range(N)]
pQueue = PriorityQueue()

# 가장자리 노드들 우선순위 큐에 넣기
for i in range(N):
    for j in range(M):
        if i == 0 or i == N - 1 or j == 0 or j == M-1:
            pQueue.put((-graph[i][j], i, j))
            visited[i][j] = True

# BFS 
for i in range(K):
    if not pQueue.empty():
        node, x, y = pQueue.get()
        
        # 수확한 옥수수 출력
        print(x+1, y+1)
    
    
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]

            # 칸 벗어남 or 이미 방문 노드 거르기
            if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny]:
                continue
            pQueue.put((-graph[nx][ny],  nx, ny))
            visited[nx][ny] = True