import sys
input = sys.stdin.readline

N = int(input().rstrip())

arr = []

for _ in range(N):
    arr.append(float(input().rstrip()))

dp = arr.copy()

for i in range(1,N):
    temp = arr[i]

    for j in range(i-1, -1, -1):
        temp = temp * arr[j]
        dp[i] = max(dp[i], temp)

print("{:.3f}".format(max(dp)))