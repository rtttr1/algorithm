import sys
input = sys.stdin.readline

N = int(input().rstrip())

arr = list(map(int, input().split()))
arr.sort()

i = 0
j = N - 1

answer = [0, N-1]

while i < j :
    if abs(arr[i] + arr[j]) < abs(arr[answer[0]] + arr[answer[1]]):
        answer = [i, j]
    if arr[i] + arr[j] > 0:
        j -= 1
    else :
        i += 1

print(arr[answer[0]], arr[answer[1]])