import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
chickens= []
house = []

for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] == 2:
            chickens.append([i,j])
        elif graph[i][j] == 1:
            house.append([i,j])

def Back(index, s):
    if len(s) == M:
        stack.append(s.copy())
        return
    for i in range(index, len(chickens)):
        s.append(chickens[i])
        Back(i+1, s)
        s.pop()

stack = []
s=[]
Back(0, s)
answer = []
for list in stack:
    sum = 0
    for home in house:
        distance = 10e9
        for chicken in list:
            distance = min((abs(chicken[0] - home[0]) + abs(chicken[1] - home[1])), distance)
        sum += distance
    answer.append(sum)
print(min(answer))
