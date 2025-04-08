import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(str, input().strip())) for _ in range(N)]

# 제곱수인지 확인하는 함수
def zegop(x):
    if x == 0 or x == 1: return True

    for i in range(1, x):
        num = i**2
        if num == x:
            return True
        if num > x: 
            return False
        
    return False

answer = -1
# (x,y)의 시작점
for x in range(N):
    for y in range(M):
        # a는 열의 등차, b는 행의 등차 의미
        for a in range(-N+1, N):
            for b in range(-M+1, M):
                num = ''
                for k in range(max(N,M)):
                    nx, ny = x + a*k, y + b*k
                    
                    if nx >= N or ny >= M or nx < 0 or ny < 0:
                        break

                    num += arr[nx][ny]
                    if zegop(int(num)):
                        answer = max(answer, int(num))
                    if zegop(int(num[::-1])):
                        answer = max(answer, int(num[::-1]))
print(answer)