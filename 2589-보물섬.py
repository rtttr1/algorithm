import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, sys.stdin.readline().strip().split(' '))

graph = [list(map(str, input().rstrip())) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
answer = 0

def BFS(a,b,visited):
    queue = deque([[a,b,0]])
    visited[b][a] = True
    max = 0

    while queue:
        x, y, count = queue.popleft()
        max = count

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N or visited[ny][nx]:
                continue 
            
            if graph[ny][nx] == 'L' :
                queue.append([nx, ny, count+1])
                visited[ny][nx] = True

    return max

for i in range(N):
    for j in range(M):
        visited = [[False]*M for _ in range(N)]
        if graph[i][j] == 'L':
            answer = max(answer, BFS(j, i, visited))
                   
print(answer)