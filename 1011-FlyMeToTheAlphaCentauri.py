import sys

T = int(sys.stdin.readline().strip())
arr = []

for i in range(T) : 
    x,y = map(int, sys.stdin.readline().strip().split(' '))
    arr.append(y-x)

def solution(r) :
    if r == 1 :
        return 1
    else :
        min = 2
        count = 1
        for i in range(2, pow(2, 31)) :
            if min <= r < min+count :
                return i
            else :
                min = min+count
                if i % 2== 0:
                    count+=1
            

for r in arr :
    print(solution(r))


