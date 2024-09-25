import sys
input = sys.stdin.readline

A = int(input().rstrip())

arr = list(map(int, input().split()))

dp = [0]*(A)

for i in range(A):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))