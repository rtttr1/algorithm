import sys
input = sys.stdin.readline
from collections import deque

N = int(input().rstrip())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
canRoot = []
for i in range(1,N+1):
    if len(graph[i]) == 3:
        canRoot.append(i)

if not canRoot: print('-1')
else:
    for root in canRoot:
        queue = deque([])
        visited = [[False]*(N+1)]
        for child in graph[root]:
            cha = 0
            for elem in graph[child]:
                
            queue.append([child, ])
        while queue:
            
            
            
            for child in graph[root]:


    
