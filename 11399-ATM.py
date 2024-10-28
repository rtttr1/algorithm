import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

answer = 0
for i in range(1, N+1):
    answer += i * arr[i-1]
print(answer)