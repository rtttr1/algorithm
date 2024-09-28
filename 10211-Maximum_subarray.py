import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    N = int(input().rstrip())
    X = list(map(int, input().split()))

    dp = X.copy()

    for i in range(1, N):
        sum = X[i]
        for j in range(i-1, -1, -1):
            dp[i] = max(dp[i], sum+X[j])
            sum += X[j]
        
    print(max(dp))