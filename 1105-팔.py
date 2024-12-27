import sys
input = sys.stdin.readline

L, R = map(str, input().split())

N = len(L)

if len(L) != len(R):
    print(0)
else:
    answer = 0
    i = 0
    while i < N:
        if L[i] == R[i]:
            if L[i] == '8' and R[i] == '8':
                answer += 1
            i += 1
        else:
            break
    print(answer) 

