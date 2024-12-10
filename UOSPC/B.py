import sys
input = sys.stdin.readline
from collections import deque

N = int(input().rstrip())
graph = [list(map(int,input().split())) for _ in range(2)]

x, y = 0, 0
answer = 0

for _ in range(N-2):
    answer += graph[x][y]
    # print(x,y,answer)
    if x == 0:
        # 양수면 먹기
        if graph[x+1][y] >= 0: 
            answer += graph[x+1][y]
            if graph[x][y+1] > graph[x+1][y+1]: x, y = x, y+1
            else: x, y = x+1, y+1
        # 세로가 음수
        else:
            # 오른쪽 양수면 그냥 가기
            if graph[x][y+1] >= 0: x, y = x, y+1
            # 오른쪽 음순데 오른쪽이 더 크면 가기
            else:
                if graph[x][y+1] > graph[x+1][y]: x, y = x, y+1
                # 오른쪽 음순데 세로가 더 큰 상황
                else:
                    if graph[x+1][y] + graph[x+1][y+1] > graph[x][y+1]: 
                        answer += graph[x+1][y]
                        x, y = x+1, y+1
                    else: x, y = x, y+1
    
    else:
        # 양수면 먹기
        if graph[x-1][y] >= 0: 
            answer += graph[x-1][y]
            if graph[x][y+1] > graph[x-1][y+1]: x, y = x, y+1
            else: x, y = x-1, y+1
        # 세로가 음수
        else:
            # 오른쪽 양수면 그냥 가기
            if graph[x][y+1] >= 0: x, y = x, y+1
            # 오른쪽 음순데 오른쪽이 더 크면 가기
            else:
                if graph[x][y+1] > graph[x-1][y]: x, y = x, y+1
                # 오른쪽 음순데 세로가 더 큰 상황
                else:
                    if graph[x-1][y] + graph[x-1][y+1] > graph[x][y+1]: 
                        answer += graph[x-1][y]
                        x, y = x-1, y+1
                        
                    else: x, y = x, y+1

answer += graph[x][y]
if x == 0:
    # 양수면 먹기
    if graph[x+1][y] >= 0: 
        answer += graph[x+1][y]
        answer += graph[x][N-1]
        if graph[0][N-1] > 0:
            answer += graph[0][N-1]
    else:
        # 오른쪽 양수면 그냥 가기
        if graph[x][y+1] >= 0: 
            answer += graph[x][y+1]
            answer += graph[x][N-1]
            # 오른쪽 음순데 오른쪽이 더 크면 가기
        else:
            if graph[x+1][y] > graph[x][y+1]:
                answer += graph[x+1][y]
                answer += graph[1][N-1]
            else:
                answer += graph[x][y+1]
                answer += graph[1][N-1]
    
else:
        # 양수면 먹기
    if graph[x-1][y] >= 0: 
        answer += graph[x-1][y]
        answer += graph[x][N-1]
        # 세로가 음수
    else:
        answer += graph[x][N-1]
    if graph[0][N-1] > 0:
        answer += graph[0][N-1]

print(answer)
