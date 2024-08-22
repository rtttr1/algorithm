import sys 
from collections import deque

M, N = map(int, sys.stdin.readline().strip(). split(' '))

graph = []
for _ in range(N) :
    graph.append(list(map(int, sys.stdin.readline().split(' '))))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def BFS (graph, arr, count) :
    queue = deque(arr)

    while queue :
        node = queue.popleft()
        
        for i in range(4) :
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]
            c = node[2]
            count = c
            if -1 < nx < M and -1 < ny < N and graph[ny][nx] == 0 :
                queue.append([nx, ny, c+1])
                graph[ny][nx] = 1

    return count

arr = []

for i in range(M) :
    for j in range(N) :
        if graph[j][i] == 1 :
            arr.append([i, j, 0])

answer = BFS(graph, arr, 0)

for i in graph :
    if 0 in i :
        answer = -1

print(answer)

        