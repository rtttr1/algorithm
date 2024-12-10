import sys
input = sys.stdin.readline

N, K = map(int, input().split())
hamper = []

for _ in range(N):
    x, y = map(int, input().split())
    hamper.append([x,y])

console = list(map(str,input().rstrip()))

x, y = 0, 0
for move in console:
    if move == 'L':
        nx, ny = x - 1, y
        if [nx, ny] not in hamper:
            x, y = nx, ny
    if move == 'R':
        nx, ny = x + 1, y
        if [nx, ny] not in hamper:
            x, y = nx, ny
    if move == 'U':
        nx, ny = x, y+1
        if [nx, ny] not in hamper:
            x, y = nx, ny
    if move == 'D':
        nx, ny = x, y-1
        if [nx, ny] not in hamper:
            x, y = nx, ny

print(x, y) 