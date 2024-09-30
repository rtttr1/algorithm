import sys
input = sys.stdin.readline

N = int(input().rstrip())

A = list(map(int, input().split()))

dp1 = [0]*N
dp2 = [0]*N
dp3 = [0]*N

for i in range(N):
    for j in range(i):
        if A[i] > A[j] and dp1[i] < dp1[j]:
            dp1[i] = dp1[j]
    dp1[i] += 1

for i in range(N-1, -1, -1):
    for j in range(N-1, i-1, -1):
        if A[i] > A[j] and dp2[i] < dp2[j]:
            dp2[i] = dp2[j]
    dp2[i] += 1

for i in range(N):
    dp3[i] = dp1[i] + dp2[i] - 1

print(max(dp3))