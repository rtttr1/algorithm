import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
arr = [[0]*M for _ in range(N)]
dx = [1,1,1,-1,-1,-1,0,0]
dy = [1,0,-1,1,0,-1,1,-1]

def BFS(sx, sy, visited):
    global arr
    q = deque([[sx,sy,0]])
    visited[sx][sy] = True

    while q:
        x, y, count = q.popleft()

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M or visited[nx][ny]:
                continue
            
            if graph[nx][ny] == 1:
                arr[sx][sy] = count+1
                return 
            else:
                visited[nx][ny] = True
                q.append([nx,ny,count+1])

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1: 
            continue
        visited = [[0]*M for _ in range(N)]
        BFS(i,j,visited)

answer = 0
for i in range(N):
    answer = max(max(arr[i]), answer)

print(answer)