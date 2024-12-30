import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))

dp = [[0]*3 for _ in range(N)]
dp[0] = arr[0]

MAX = 10e9
answer = MAX

for k in range(3):
    dp = [[MAX]*3 for _ in range(N)]
    dp[0][k] = arr[0][k]

    for i in range(1, N):
        for j in range(3):
            dp[i][j] = arr[i][j] + min(dp[i-1][(j+1)%3], dp[i-1][(j+2) % 3])
    
    for i in range(3):
        if k != i:
            answer = min(answer, dp[-1][i])

print(answer)
