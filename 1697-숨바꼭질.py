import sys

from collections import deque

N, K = map(int, sys.stdin.readline().strip().split(' '))

visited = set([N])

def BFS(start, goal) :
    queue = deque([[start, 0]])

    while queue :
        x, count = queue.popleft()
        
        if x == goal :
            return count 
        
        for nx in [x-1, x+1, x*2] :
           if nx < 0 or nx > 200000 :
                continue 
           elif nx not in visited :
                queue.append([nx, count + 1])
                visited.add(nx)
        
print(BFS(N, K))