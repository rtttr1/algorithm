import sys

input = sys.stdin.readline

N = int(input().rstrip())

dp = [0]*(N+1)

if N == 1 :
    print(0)
else :
    for i in range(2, N+1):
        if i % 3 == 0 and i % 2 == 0:
            dp[i] = min(dp[int(i//2)], dp[int(i//3)], dp[int(i-1)]) + 1
        elif i % 3 == 0:
            dp[i] = min(dp[int(i//3)], dp[int(i-1)]) + 1
        elif i % 2 == 0:
            dp[i] = min(dp[int(i//2)], dp[int(i-1)]) + 1    
        else :
            dp[i] = dp[i-1] + 1
    print(dp[N])
