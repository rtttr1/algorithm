import sys
input = sys.stdin.readline
from collections import deque

# hiper는 0부터, 역은 1부터
# 역, 연결된 역의 수, 하이퍼튜브 수
N, K, M = map(int, input().split()) 
hiperToStation = [list(map(int, input().split())) for _ in range(M)]
visitedHiper = [False]*(M)
visitedStation = [False]*(N+1)
stationToHiper = [[] for _ in range(N+1)]

for i in range(M):
    for j in range(K):
        stationToHiper[hiperToStation[i][j]].append(i)

answer = -1

def BFS():
    global answer
    q = deque([[1,1]])
    visitedStation[1] = True

    while q:
        now, count = q.popleft()
        
        # 환승할 수 있는 하이퍼튜브 구하기
        canHiper = []
        for hiper in stationToHiper[now]:
            if not visitedHiper[hiper]:
                canHiper.append(hiper)
                visitedHiper[hiper] = True

        # 갈 수 있는 역 구하기
        for hiper in canHiper:
            for station in hiperToStation[hiper]:
                if not visitedStation[station]:
                    if station == N:
                        answer = count + 1
                        return
                    q.append([station, count+1])
                    visitedStation[station] = True

if N == 1:
    print(1)
else:
    BFS()
    print(answer)