import sys
input = sys.stdin.readline

n = int(input().rstrip())

graph = []
dp = [[0]*n for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    graph.append(list(map(int, input().split())))

def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]
    
    dp[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        
        if graph[nx][ny] > graph[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny)+1)

    return dp[x][y]
    
for i in range(n):
    for j in range(n):
        if dp[i][j] == 0:
            dfs(i, j)

answer = 0
for i in range(n):
    answer = max(answer, max(dp[i]))
print(answer)
