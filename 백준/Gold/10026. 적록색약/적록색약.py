import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())
graph = list(list(map(str, input().rstrip())) for _ in range(N))
visited = [[False]*N for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
answer = 0
answer2 = 0
def BFS(start, color):
    queue = deque([start])

    while queue:
        node = queue.popleft()
        
        for i in range(4):
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny]: 
                continue

            if graph[nx][ny] in color:
                queue.append([nx,ny])
                visited[nx][ny] = True

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS([i,j], [graph[i][j]])
            answer += 1

visited = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            if graph[i][j] == 'B':
                BFS([i,j], ['B'])
                answer2 += 1
            else:
                BFS([i,j], ['R', 'G'])
                answer2 += 1
           

print(answer, answer2)