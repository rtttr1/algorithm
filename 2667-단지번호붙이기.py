import sys 
from collections import deque

N = int(sys.stdin.readline().strip())

graph = []

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(N) :
    graph.append(list(map(int, sys.stdin.readline().strip())))

result=[] 

def BFS(graph, x, y) :
    queue = deque([[x,y]])
    graph[y][x] = 0
    count = 1

    while queue : 
        node = queue.popleft()
        for i in range(4) :
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]

            if -1 < nx < N and -1 < ny < N and graph[ny][nx] == 1:
                queue.append([nx, ny])
                graph[ny][nx] = 0
                count+=1

    return count 

for i in range(N) :
    for j in range(N) :
        if graph[i][j] == 1 :
            result.append(BFS(graph,j,i))

result.sort()

print(len(result))

for i in result:
    print(i)

