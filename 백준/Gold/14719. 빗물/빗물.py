import sys
input = sys.stdin.readline

H, W = map(int, input().split())
arr = list(map(int, input().split()))

result = 0

for i in range(1, W-1):
    left = max(arr[:i])
    right = max(arr[i+1:])

    if min(left, right) > arr[i]:
        result += (min(left, right) - arr[i])

print(result)