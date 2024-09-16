import sys
input = sys.stdin.readline

n = int(input().rstrip())

dp = [0]*(n+1)
if n == 0 :
    print(1)
else :
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2] + 1

    print(dp[-1] % 1000000007)
