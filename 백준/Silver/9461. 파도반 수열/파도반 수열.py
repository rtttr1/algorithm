import sys
input = sys.stdin.readline

T = int(input().rstrip())
dp = [0]*(101)
dp[0:6] = [0,1,1,1,2,2]

for i in range(6, 101):
    dp[i] = dp[i-1] + dp[i-5]
 
for _ in range(T):
    N = int(input().rstrip())
    print(dp[N])