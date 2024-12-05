import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().split()))
M = int(input().rstrip())

dp = [[0]*N for _ in range(N)]

for i in range(N):
    dp[i][i] = 1
for i in range(N-1):
    if arr[i] == arr[i+1]: 
        dp[i][i+1] = 1
for cnt in range(N-2):
    for i in range(N-2-cnt):
        j = i + cnt + 2
        if arr[i] == arr[j] and dp[i+1][j-1] == 1:
            dp[i][j] = 1
        
for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S-1][E-1])
