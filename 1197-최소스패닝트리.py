import sys 
input = sys.stdin.readline

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0 :
        break
    if a > b: print('Yes')
    else: print('No')
V, E = map(int, input().split())
graph = [[]]*(V+1)

for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append([B,C])
    graph[B].append([A,C])
