import sys
input = sys.stdin.readline

T = int(input().rstrip())

dp = [0]*41
dp[1] = 1

for i in range(2, 41):
    dp[i] = dp[i-1] + dp[i-2]

for _ in range(T):
    N = int(input().rstrip())
    if N == 0:
        print(1, 0)
    elif N == 1:
        print(0, 1)
    else: 
        print(dp[N-1], dp[N])