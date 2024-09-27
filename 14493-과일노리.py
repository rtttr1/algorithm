import sys
input = sys.stdin.readline

N = int(input().rstrip())

answer = 0
for _ in range(N):
    a, b = map(int, input().split())

    if answer == 0:
        answer += (b+1)
    else:
        n = answer % (a+b)
        if n < b:
            answer += (b-n+1)
        else:
            answer += 1
        
print(answer)
