import sys
input = sys.stdin.readline

N = int(input().rstrip())

arr = list(map(int, input().split()))
arr.sort()
answer = 0

for i in range(N):
    start, end = 0, N-1

    while start < end:
        if start == i:
            start += 1
            continue
        elif end == i:
            end -= 1
            continue

        if arr[start] + arr[end] == arr[i]:
            answer += 1
            break
        elif arr[start] + arr[end] > arr[i]:
            end -= 1
        elif arr[start] + arr[end] < arr[i]:
            start += 1
    
print(answer)
