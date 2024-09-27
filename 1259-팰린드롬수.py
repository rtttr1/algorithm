import sys
input = sys.stdin.readline

while True:
    N = list(input().rstrip())

    if N[0] == '0':
        break
    else:
        n = len(N)
        answer = 'yes'

        for i in range(n):
            if N[i] != N[n-i-1]:
                answer = 'no'
                continue
        print(answer)

