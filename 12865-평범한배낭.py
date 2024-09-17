import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0]*(K+1) for _ in range(N+1)]
arr = [[0,0]]

for _ in range(N):
    arr.append(list(map(int, input().split())))
arr = sorted(arr)

for i in range(1,N+1):
    w, v = arr[i][0], arr[i][1]
    for j in range(1, K+1):
        if w > j:
            dp[i][j] = dp[i-1][j]
        else :
            dp[i][j] = max(dp[i-1][j], v + dp[i-1][j-w])

print(dp[N][-1])

