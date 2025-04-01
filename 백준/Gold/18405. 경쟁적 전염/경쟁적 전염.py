import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

dx = [1,0,-1,0]
dy = [0,1,0,-1]

initialArr = []
for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                 initialArr.append([arr[i][j], i, j, 0])
initialArr.sort()

def BFS():
    q = deque(initialArr)
    
    while q:
        n, x, y, s = q.popleft()
        # S초가 지나면 탈출
        if s == S:
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
            if arr[nx][ny] == 0:
                arr[nx][ny] = n
                q.append([n, nx, ny, s+1])
BFS()
print(arr[X-1][Y-1])