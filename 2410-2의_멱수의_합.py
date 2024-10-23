import sys
input = sys.stdin.readline

N = int(input().rstrip())

dp = [0]*(N+1)
dp[0:5] = [0,1,2,2,4]

for i in range(5, N+1):
    if i % 2 == 0 :
        if (i//2) % 2 == 1:
            dp[i] = dp[i-2] + dp[i//2 - 1]
        else :
            dp[i] = dp[i-2] + dp[i//2]
    else:
        dp[i] = dp[i-1]


print(dp[N] % 1000000000)