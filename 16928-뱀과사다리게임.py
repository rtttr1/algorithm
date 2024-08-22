import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split(' '))

graph = [i for i in range(100)]

for _ in range(N+M) :
   x, y = map(int, sys.stdin.readline().strip().split(' '))
   graph[x-1] = y-1

def BFS(graph) :
    queue = deque([[0, 0]])
    
    while queue : 
        arr = []
        x , count = queue.popleft()
        next = []

        for i in range(1, 7) :
            if x+i < 100 :
                if x+i != graph[x+i] :
                    next.append(graph[x+i])
                else :
                    arr.append(graph[x+i])
        next.append(max(arr))

        for i in next :
            if i == 99 :
                count += 1
                return count
            else :
                queue.append([i, count+1])

print(BFS(graph))