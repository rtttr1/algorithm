import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().split()))

arr.sort()

S = sum(arr)

for i in range(N):
    if S*(-1) <= arr[i]:
        break
    else:
        S += (S*(-1) - arr[i])
        arr[i] = S*(-1)

print(S)