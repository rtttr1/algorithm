import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
arr= [list(map(int,input().split())) for _ in range(N)]

dp = [[0]*(H+1) for _ in range(N)]

for elem in arr[0]:
    dp[0][elem] = 1

for i in range(1, N):
    for j in range(H+1):
        dp[i][j] = dp[i-1][j]
        for k in arr[i]:
            # 블록의 높이가 탑을 넘어가면 탈출
            if k > j: break
            # 블록의 높이가 탑의 높이면 + 1
            if k == j: dp[i][j] += 1
            dp[i][j] += dp[i-1][j-k]

print(dp[-1][-1] % 10007)              