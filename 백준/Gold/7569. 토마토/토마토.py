import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())

graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False]*M]*N]*H

# 위, 아래, 상, 하, 좌, 우 
dx = [1,0,-1,0,0,0]
dy = [0,1,0,-1,0,0]
dz = [0,0,0,0,1,-1]
answer = 0

queue = deque()
# 1 넣기
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                queue.append([k,j,i,0])

# BFS
while queue:
    x, y, z, day = queue.popleft()
    
    answer = max(day, answer)
    for i in range(6):
        nx = dx[i] + x
        ny = dy[i] + y
        nz = dz[i] + z

        if nx < 0 or ny < 0 or nz < 0 or nx >= M or ny >= N or nz >= H or graph[nz][ny][nx] != 0: continue
        if graph[nz][ny][nx] == 0:
            graph[nz][ny][nx] = 1
            queue.append([nx,ny,nz, day + 1])

# 최종 답 체크
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0:
                answer = -1
print(answer)
        
