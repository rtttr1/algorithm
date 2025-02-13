import sys
input = sys.stdin.readline

N = int(input().rstrip())

arr = list(map(int, input().split()))
M = max(arr)

checked = [False]*(M+1)
scores = [0]*(M+1)

for elem in arr:
    checked[elem] = True

for elem in arr:
    j = 2
    while elem*j <= M:
        if checked[elem*j]:
            scores[elem] += 1
            scores[elem*j] -= 1
        j += 1

for elem in arr:
    print(scores[elem], end=' ')
