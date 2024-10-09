import sys
from collections import deque
input = sys.stdin.readline

graph = [list(input().rstrip()) for i in range(12)]
answer = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]
visited = [[False]*6 for _ in range(12)]

def BFS(x, y):
    queue = deque([(x, y)])
    now = graph[x][y]
    pos = []

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6 and graph[nx][ny] == now and not visited[nx][ny]:
                pos.append((nx, ny))
                queue.append((nx, ny))
                visited[nx][ny] = 1

    if len(pos) >= 4:
        pos.sort(key=lambda x: (x[1], x[0]))
        for i, j in pos:
            graph[i][j] = '_'
            nodeArr.append((i, j))

while True:
    visited = [[0] * 6 for _ in range(12)]
    nodeArr = []

    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.' and graph[i][j] != '_' and not visited[i][j]:
                BFS(i, j)

    if len(nodeArr) == 0:
        break

    for node in nodeArr:
        x, y = node[0], node[1]
        for i in range(x, 0, -1):
            graph[i][y] = graph[i-1][y]
        graph[0][y] = '.'

    answer += 1

print(answer)