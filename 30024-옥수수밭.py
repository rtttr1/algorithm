import sys
input = sys.stdin.readline
from collections import deque
from queue import PriorityQueue

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
K = int(input().rstrip())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[False]*M for _ in range(N)]
pQueue = PriorityQueue()

for i in range(N):
    pQueue.put(graph[0, i])
    pQueue.put(graph[M, i])
for j in range(1, M-1):
    pQueue.put(graph[j, 0])
    pQueue.put(graph[j, N])

def BFS():
    queue = deque([[-1, -1, 0]])

    while queue:
        x, y, count = queue.popleft()

        if count == K:
            return count
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > M or ny < 0 or ny > N or visited[ny][nx] == True:
                continue
            if 
            
            



