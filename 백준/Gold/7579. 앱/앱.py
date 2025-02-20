import sys 
input = sys.stdin.readline

N, M = map(int, input().split())

memories = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))

K = sum(costs)
answer = 10e9
dp = [[0]*(K+1) for _ in range(N+1)]

# i 는 물건 번째
for i in range(1, N+1):
    # j는 최대 코스트
    for j in range(K+1):
        if costs[i] <= j:
            dp[i][j] = max(dp[i-1][j], memories[i] + dp[i-1][j-costs[i]])
        else:
            dp[i][j] = dp[i-1][j]
        if dp[i][j] >= M:
            answer = min(answer, j)

print(answer)