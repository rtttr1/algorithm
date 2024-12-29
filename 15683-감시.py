import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

count = 0
cctvs = []
for i in range(N):
    for j in range(M):
        if 0 < graph[i][j] < 6:
            count += 1
            cctvs.append([graph[i][j], i, j])

arr = []

def back(cctv):
    if len(cctv) == count:
        arr.append(cctv.copy()[::-1])
        return
    
    if cctvs[len(cctv)-1][0] == 5:
        cctv.append(0)
        back(cctv)
        return
    
    for i in range(4):
        cctv.append(i)
        back(cctv)
        cctv.pop()

temp = []
back(temp)

