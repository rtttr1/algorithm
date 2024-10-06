import sys
input = sys.stdin.readline

N = int(input().rstrip())
price = list(map(int, input().split()))
dp = [0]*(N+1)

for i in range(1, N+1):
    MAX = price[i-1]
    for j in range(i):
        if MAX < dp[j] + dp[i-j]:
            MAX = dp[j] + dp[i-j]
    dp[i] = MAX

print(max(dp))