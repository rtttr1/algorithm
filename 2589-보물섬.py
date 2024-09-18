import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, sys.stdin.readline().strip().split(' '))

graph = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[False]*M for _ in range(N)]

for i in range(N) :
    graph.append(list(map(str, input().rstrip())))

def BFS(visited):
    queue = deque([[0,0,0]])

    while queue:
        x, y, count = queue.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] != 'W' and not visited[ny][nx] :
                queue.append([nx, ny, count+1])
                