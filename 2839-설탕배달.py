import sys
input = sys.stdin.readline

N = int(input().strip())

graph = [-1]*5001
graph[3] = 1
graph[5] = 1

for i in range(6, 5001):
    if graph[i-3] > 0 and graph[i-5] > 0:
        graph[i] = min(graph[i-3], graph[i-5])+1
    elif graph[i-5] > 0 :
        graph[i] = graph[i-5]+1
    elif graph[i-3] > 0 :
        graph[i] = graph[i-3]+1

print(graph[N])
