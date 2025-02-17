import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
answer = 0
circle = 1

for _ in range(N):
    arr.append(list(map(str, input().rstrip())))
visited = [[0]*M for _ in range(N)]


def direct(x, y, d):
    if d == 'D':
        return x+1, y
    elif d == 'U':
        return x-1, y
    elif d == 'L':
        return x, y-1
    elif d == 'R':
        return x, y+1

def DFS(x, y, num):
    global answer
    # 사이클이 형성되었을때
    if visited[x][y] == num: 
        answer += 1
        return
    # 다른 사이클에 도달했을때
    if visited[x][y] != num and visited[x][y] != 0:
        return
    visited[x][y] = num

    nx, ny = direct(x,y,arr[x][y])
    DFS(nx, ny, num)

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            DFS(i,j,circle)
            circle += 1

print(answer)