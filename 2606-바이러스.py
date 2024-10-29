import sys
input = sys.stdin.readline
from collections import deque

N = int(input().rstrip())
E = int(input().rstrip())
graph = [[] for _ in range(N+1)]

for i in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])
arr = [1]
answer = 0
while queue:
    node = queue.popleft()
    for computer in graph[node]:
        if computer not in arr:
            queue.append(computer)
            arr.append(computer)
            answer+=1

print(answer)
