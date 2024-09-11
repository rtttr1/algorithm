import sys
from collections import deque

input = sys.stdin.readline

tooth = []
top = [0,0,0,0]

for _ in range(4):
    tooth.append(list(map(int,input().rstrip())))

K = int(input().rstrip())

queue = deque([])


for i in range(K):
    temp = list(map(int, input().split()))
    visited = [False]*4
    visited[temp[0]-1] = True
    queue.append(temp)

    while queue:
        n, turn = queue.popleft()
        print(n, turn)

        if n-2 > -1 and tooth[n-2][top[n-2]+2] != tooth[n-1][top[n-1]-2] and not visited[n-1] :
            top[n-2] -= turn
            queue.append([n-2, -turn])
            visited[n-2] = True
        elif n < 4 and tooth[n][top[n]-2] != tooth[n-1][top[n-1]+2] and not visited[n-1] :
            top[n] -= turn
            queue.append([n, -turn])
            visited[n] = True
        top[n-1] += turn

print(top)
sum = 0
for i in range(4):
    if tooth[i][top[i]] == 1:
        sum += pow(2,i)
print(sum)









       
        
                
                    

                
