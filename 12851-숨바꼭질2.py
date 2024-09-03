import sys

from collections import deque

N, K = map(int, sys.stdin.readline().strip().split(' '))

visited = [-1]*(100001)
visited[N] = 0

def BFS(start, goal) :
    queue = deque([start])
    way = 0

    while queue :
        x = queue.popleft()
        
        if x == goal:
            way+=1
        
        for nx in [x-1, x+1, x*2] :
           if nx < 0 or nx > 100000 :
                continue 
           elif visited[nx] == visited[x] + 1 or visited[nx] == -1 :
                queue.append(nx)
                visited[nx] = visited[x] + 1
    return visited[K], way

a, b = BFS(N, K)

print(a)
print(b)