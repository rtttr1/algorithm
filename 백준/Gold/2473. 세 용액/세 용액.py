import sys
input = sys.stdin.readline

N = int(input().rstrip())

arr = list(map(int, input().split()))
arr.sort()

total = 10e9
answer = []

for left in range(N):
    mid = left + 1
    right = N-1

    while mid < right:
        sum = arr[left] + arr[mid] + arr[right]
        if abs(sum) < abs(total):
            total = sum
            answer = [arr[left], arr[mid], arr[right]]
        if sum > 0: 
            right -= 1
        else:
            mid += 1
print(' '.join(str(s) for s in answer))
