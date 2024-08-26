import sys

N, M = map(int, sys.stdin.readline().strip().split(' '))

def DFS(N, M, result):
    if len(result) == M :
        for i in result :
            print(i, end = ' ')
        print()
    for i in range(1, N+1):
        if i not in result:
            result.append(i)
            DFS(N, M, result)
            result.pop()

DFS(N,M,[])