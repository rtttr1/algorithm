import sys
input = sys.stdin.readline

N = int(input().rstrip())
list = []
dp = [1]*N

for i in range(N):
    start, end = map(int, input().split())
    list.append([start, end])

list.sort()

for i in range(1, N):
    for j in range(0,i):
        if list[j][1] < list[i][1] :
            dp[i] = max(dp[i], dp[j]+1)

print(N-max(dp))