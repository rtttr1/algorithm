import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = []
dp = [0]*(n+1)
arr.append(0)

for _ in range(n): 
    arr.append(int(input().rstrip()))

if n == 1:
    print(arr[1])
elif n == 2:
    print(arr[1]+arr[2])
else:
    dp[1] = arr[1]
    dp[2] = arr[1] + arr[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i-1], dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i])

    print(dp[-1])
    