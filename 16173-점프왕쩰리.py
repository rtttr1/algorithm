import sys 
from collections import deque

N = int(sys.stdin.readline().strip())

graph = []
for _ in range(N) :
    graph.append(list(map(int, sys.stdin.readline().split(' '))))

visited = [[False]*3 for _ in range(N)]

dx = [1, 0]
dy = [0, 1]

def BFS(graph) :
    queue = deque([[0,0]])
    
    while queue :
        x, y = queue.popleft()
        
        if graph[y][x] == -1 : 
            return "HaruHaru"

        for i in range(2) :
            nx = x + dx[i]*graph[y][x]
            ny = y + dy[i]*graph[y][x]
            
            if -1 < nx < N and -1 < ny < N and not visited[ny][nx]:
                queue.append([nx, ny])
                visited[ny][nx] = True

    return "Hing"

print(BFS(graph))