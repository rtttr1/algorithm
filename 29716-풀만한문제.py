import sys
input = sys.stdin.readline

J, N = map(int, input().split())
answer = 0

for _ in range(N):
    arr = str(input().rstrip())
    sum = 0
    for elem in arr :
        if 97 <= ord(elem) <= 122 or 48 <= ord(elem) <= 57:
            sum += 2
        elif 65 <= ord(elem) <= 90:
            sum += 4
        else:
            sum += 1
    if sum <= J :
        answer += 1

print(answer)

