import sys 
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split(' '))

graph = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(N) :
    graph.append(list(map(int, sys.stdin.readline().strip())))


def BFS(graph, goal) :
    queue = deque([[0, 0, 1]])
    graph[0][0] = 0
    while queue:
        now = queue.popleft()

        if now[0] == goal[0]-1 and now[1] == goal[1]-1 :
            return now[2] 
        
        for i in range(4) :
            x = now[0] + dx[i]
            y = now[1] + dy[i]
            count = now[2]
            if x > -1 and y > -1 and x < goal[0] and y < goal[1] and graph[y][x] == 1: 
                queue.append([x,y,count+1])
                graph[y][x] = 0
            
print(BFS(graph, [M,N]))

