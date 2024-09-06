import sys
input = sys.stdin.readline

N, M, q = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

for _ in range(q):
    query = list(map(int, input().split()))
    
    if query[0] == 0 :
        graph[query[1]][query[2]] = query[3]
    else :
        graph[query[1]], graph[query[2]] = graph[query[2]], graph[query[1]]

for elem in graph:
    for e in elem :
        print(e, end=' ')
    print()