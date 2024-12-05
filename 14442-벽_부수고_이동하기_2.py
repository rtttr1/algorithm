import sys
input = sys.stdin.readline
from collections import deque

N, M, K = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[False]*(M) for _ in range(N)] for _ in range(K+1)]

N, M = N-1, M-1
dx = [1,0,-1,0]
dy = [0,1,0,-1]
answer = 10e9

def bfs(visited):
    global answer
    queue = deque([[0,0,1,0]])
    visited[0][0][0] = True
    
    while queue:
        x, y, count, broken = queue.popleft()
        
        if x == N and y == M:
            answer = min(answer, count)
            continue

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if nx < 0 or nx > N or ny < 0 or ny > M or visited[broken][nx][ny]: 
                continue

            if graph[nx][ny] == 0:
                visited[broken][nx][ny] = True
                queue.append([nx,ny,count+1,broken])
                continue

            if graph[nx][ny] == 1 and broken < K:
                visited[broken][nx][ny] = True
                queue.append([nx,ny,count+1,broken+1])
                continue
            
bfs(visited)
if answer == 10e9: print(-1)
else: print(answer)
