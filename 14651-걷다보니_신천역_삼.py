import sys
input = sys.stdin.readline

N = int(input().rstrip())

dp = [0]*(N+1)
if N == 1:
    print(0)
elif N == 2:
    print(2)
else:
    dp[2] = 2
    for i in range(3, N+1):
        dp[i] = dp[i-1]*3
    print(dp[-1] % 1000000009)

