import sys
from collections import deque
input = sys.stdin.readline

T = int(input().rstrip())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(T):
    H, W = map(int, sys.stdin.readline().strip().split(' '))
    graph = []
    for _ in range(H):
        graph.append(list(map(str, input().rstrip())))
    count = 0
    for i in range(H):
        for j in range(W) :
            if graph[i][j] == '#':
                count += 1
                queue = deque([[j, i]])
                graph[i][j] = '.'

                while queue:
                    x, y = queue.pop()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if nx < 0 or W <= nx or ny < 0 or H <= ny:
                            continue
                        if graph[ny][nx] == '#':
                            queue.append([nx, ny])
                            graph[ny][nx] = '.'

    print(count)