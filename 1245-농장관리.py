import sys 
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

nx = [1, 0, -1, 0, 1, 1, -1, -1]
ny = [0, 1, 0, -1, -1, 1, -1, 1]
visited = [[False]*M for _ in range(N)]

def BFS(a, b, h):
    isSanbong = True
    queue = deque([[a, b, h]])
    visited[a][b] = True

    while queue:
        x, y, height = queue.popleft()

        for i in range(8):
            dx, dy = x + nx[i], y + ny[i]
            
            if dx < 0 or dx >= N or dy < 0 or dy >= M: continue

            if graph[dx][dy] > height:
                isSanbong = False
            elif graph[dx][dy] == height and not visited[dx][dy]:
                queue.append([dx,dy,height])
                visited[dx][dy] = True
            
    return isSanbong

answer = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            result = BFS(i,j,graph[i][j])
            if result: answer += 1

print(answer)