import sys
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())

arr = list(map(int, input().split()))
max = 0
for i in range(M-1):
    if arr[i+1] - arr[i] > max:
        max = arr[i+1] - arr[i]

temp = arr[0] if arr[0] > N-arr[-1] else N-arr[-1]

if max % 2 == 0:
    if temp > max // 2:
        print(temp)
    else:
        print(max//2)
else:
    if temp > max // 2 + 1:
        print(temp)
    else:
        print(max//2+1)

