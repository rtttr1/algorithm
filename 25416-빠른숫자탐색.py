import sys
from collections import deque

graph = []
for _ in range(5) :
    graph.append(list(map(int, sys.stdin.readline().strip().split(' '))))

r, c = map(int, sys.stdin.readline().strip().split(' '))
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def BFS(graph, r, c):
    queue = deque([[r,c,0]])
    graph[r][c] = -1

    while queue :
        x, y, count = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if -1 < nx < 5 and -1 < ny < 5 :
                if graph[nx][ny] == 0 :
                    queue.append([nx, ny, count+1])
                    graph[nx][ny] = -1
                elif graph[nx][ny] == 1 :
                    return count+1
    return -1

print(BFS(graph, r, c))

