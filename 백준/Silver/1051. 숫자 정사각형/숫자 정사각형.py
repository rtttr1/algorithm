import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

answer = 1
def search(x, y):
    global answer
    num = graph[x][y]
    
    for i in range(x+1, N):
        if graph[i][y] == num:
            cm = i - x
            if cm + y < M and graph[x][y+cm] == num and graph[i][y+cm] == num:
                answer = max(answer, (cm+1)**2)

for x in range(N):
    for y in range(M):
        search(x,y)

print(answer)