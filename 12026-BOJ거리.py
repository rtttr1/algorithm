import sys
input = sys.stdin.readline
INF = 1e9

N = int(input().rstrip())
block = [0]
block[1:] = list(map(str, input().rstrip()))

dp = [INF]*(N+1)
dp[1] = 0

for i in range(2,N+1):
    if block[i] == 'B':
        for j in range(1, i):
            if block[j] == 'J':
                dp[i] = min(dp[i], dp[j] + pow(i-j, 2))
    elif block[i] == 'O':
        for j in range(1, i):
            if block[j] == 'B':
                dp[i] = min(dp[i], dp[j] + pow(i-j, 2))
    elif block[i] == 'J':   
        for j in range(1, i):
            if block[j] == 'O':
                dp[i] = min(dp[i], dp[j] + pow(i-j, 2))

if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])