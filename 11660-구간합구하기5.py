import sys

N, M = map(int, sys.stdin.readline().strip().split(' '))

graph = []
for i in range(N) :
    graph.append(list(map(int, sys.stdin.readline().strip().split(' '))))

node = []
for i in range(M) :
    node.append(list(map(int, sys.stdin.readline().strip().split(' '))))

sum = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1) :
    for j in range(1, N+1) :
        sum[i][j] = sum[i][j-1] + sum[i-1][j] - sum[i-1][j-1] + graph[i-1][j-1]

for i in range(M) :
    x1, y1, x2, y2 = node[i]
    print(sum[x2][y2] - sum[x2][y1-1] - sum[x1-1][y2] + sum[x1-1][y1-1])