import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[False]*2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = True
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def BFS():
    queue = deque([[0,0,1,0]])

    while queue:
        x, y, count, z = queue.popleft()

        if x == M-1 and y == N-1:
            return count

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if graph[ny][nx] == 0 and not visited[ny][nx][z]:
                queue.append([nx, ny, count+1, z])
                visited[ny][nx][z] = True
            elif graph[ny][nx] == 1 and z == 0:
                queue.append([nx, ny, count+1, 1])
                visited[ny][nx][1] = True

    return -1

print(BFS())

