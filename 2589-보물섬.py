import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, sys.stdin.readline().strip().split(' '))

graph = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
answer = 100000000000

for i in range(N) :
    graph.append(list(map(str, input().rstrip())))

def BFS(a,b,visited):
    queue = deque([[a,b,0]])
    max = 0
    while queue:
        x, y, count = queue.pop()
        max = count

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 'L' and not visited[ny][nx] :
                queue.append([nx, ny, count+1])
                visited[ny][nx] = True
    return max

for i in range(N):
    for j in range(M):
        visited = [[False]*M for _ in range(N)]
        if graph[i][j] == 'L':
            temp = BFS(j, i, visited) 
            print(temp)
            if temp < answer:
                answer = temp
            
        
print(answer)