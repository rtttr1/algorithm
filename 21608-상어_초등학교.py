import sys
input = sys.stdin.readline

N = int(input().rstrip())

like = []
school = [[0]*N for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

for _ in range(pow(N,2)):
    temp = list(map(int, input().split()))
    like.append([temp[0], temp[1:]])


for info in like:
    student, friends = info[0], info[1]
    final = []
    for i in range(N):
        for j in range(N):
            if school[i][j] != 0:
                continue
            empty = 0
            prefer = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if school[nx][ny] == 0:
                    empty += 1
                elif school[nx][ny] in friends:
                    prefer += 1
            final.append([prefer, empty, i, j])
    final.sort(key=lambda x:(-x[0], -x[1], x[2], x[3]))
    school[final[0][2]][final[0][3]] = student

answer = 0
like.sort()
for i in range(N):
    for j in range(N):
        people = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if school[nx][ny] in like[school[i][j]-1][1]:
                people+=1
        
        if people != 0:
            answer += 10**(people-1)
        
print(answer)
        