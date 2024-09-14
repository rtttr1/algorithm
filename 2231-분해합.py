import sys

input = sys.stdin.readline

N = int(input().rstrip())

answer = 0
for i in range(1, N):
    l = list(map(int, str(i)))
    sum = i
    for elem in l :
        sum += elem

    if sum == N :
        answer = i
        break

print(answer)

