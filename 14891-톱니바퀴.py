import sys
from collections import deque
input = sys.stdin.readline

tooth = [deque(list(map(int, input().rstrip()))) for _ in range(4)]
K = int(input().rstrip())

# K번 회전
for _ in range(K):
    default = []
    for i in range(4):
        default.append([tooth[i][6], tooth[i][2]])
    number, turn = map(int, input().split())
    number -= 1

    if number > 0:
        for i in range(number, 0, -1):
            if default[i][0] != default[i-1][1]:
                if (number-(i-1)) % 2 == 0:
                    tooth[i-1].rotate(turn)
                else:
                    tooth[i-1].rotate(turn*(-1))
            else:
                break
    
    if number < 3:
        for i in range(number, 3):
            if default[i][1] != default[i+1][0]:
                if (number-(i+1)) % 2 == 0:
                    tooth[i+1].rotate(turn)
                else:
                    tooth[i+1].rotate(turn*(-1))
            else:
                break
    
    tooth[number].rotate(turn)

answer = 0
if tooth[0][0] == 1:
    answer +=1    
if tooth[1][0] == 1:
    answer +=2    
if tooth[2][0] == 1:
    answer +=4   
if tooth[3][0] == 1:
    answer +=8    

print(answer)


    



