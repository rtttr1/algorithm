import sys
input = sys.stdin.readline

arr1 = list(map(str, input().rstrip()))
arr2 = list(map(str, input().rstrip()))
N = len(arr1)
M = len(arr2)

dp = [[0]*(N+1) for _ in range(M+1)]

for i in range(1,M+1):
    for j in range(1,N+1):
        if arr2[i-1] == arr1[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])
