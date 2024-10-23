import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dp = [[0]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    dp[i][1:] = list(map(int, input().split(' ')))

for r in range(1, N+1):
    for c in range(1, M+1):
        dp[r][c] = dp[r][c] + max(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])

print(dp[-1][-1])