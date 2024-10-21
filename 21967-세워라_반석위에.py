import sys
input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().split()))

i, j = 0,1
answer = 0
MIN, MAX = min(A[i:j+1]), max(A[i:j+1])

while j < N:
    MIN = min(A[i:j+1])
    MAX = max(A[i:j+1])

    if MAX - MIN > 2:
        i += 1
    else:
        if answer < j-i+1: answer = j-i+1
        j += 1

print(answer)