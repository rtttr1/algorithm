import sys
from collections import deque

input = sys.stdin.readline

C, R = map(int, input().split())

graph = [list(map(str, input().rstrip())) for _ in range(C)]
fireGraph = graph.copy()
visited = [[False]*R for _ in range(C)]

answer = False
dx = [1,0,-1,0]
dy = [0,1,0,-1]
    
# 준비 단계
fireArr = []
for i in range(R):
    for j in range(C):
        if graph[j][i] == 'J':
            start = [i, j]
        if graph[j][i] == 'F':
            fireArr.append([i, j])

queue = deque()
for elem in fireArr:
    queue.append([elem[0], elem[1], -1])
queue.append([start[0], start[1], 1])
visited[start[0]][start[1]] = True

# BFS 돌기 
while queue:
    x, y, count = queue.popleft()

    if count > 0 and (x == R-1 or  x == 0 or y == 0 or y == C-1):
        answer = count 
        break
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        if count > 0:
            if graph[ny][nx] == '.' and not visited[ny][nx]: 
                queue.append([nx,ny,count+1])
                visited[ny][nx] = True
        else:
            if graph[ny][nx] == '.': 
                queue.append([nx,ny,-1])
                graph[ny][nx] = 'F'

if not answer:
    print("IMPOSSIBLE")
else:
    print(answer)



