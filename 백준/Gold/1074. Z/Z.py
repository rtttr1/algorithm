import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())
answer = 0

while N >= 0:
    if pow(2, N-1) > r and pow(2, N-1) > c:
        answer += pow(2, N-1)*pow(2,N-1)*0
    elif pow(2, N-1) > r and pow(2, N-1) <= c:
        answer += pow(2, N-1)*pow(2,N-1)
        c -= pow(2, N-1)
    elif pow(2, N-1) <= r and pow(2, N-1) > c:
        answer += pow(2, N-1)*pow(2,N-1)*2
        r -= pow(2, N-1)
    elif pow(2, N-1) <= r and pow(2, N-1) <= c:
        answer += pow(2, N-1)*pow(2,N-1)*3
        c -= pow(2, N-1)
        r -= pow(2, N-1)
  
    N -= 1
    

print(int(answer))

    