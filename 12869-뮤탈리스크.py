import sys 
from collections import deque

N = int(sys.stdin.readline().strip())

HP = list(map(int, sys.stdin.readline().strip().split(' ')))

attack = [9, 3, 1]

def BFS(N, HP) :
    count = 0
    
    while True :
        HP.sort(reverse=True)
        
        for i in range(N) :
            if HP[i] > -1 :
                HP[i] -= attack[i]
        count += 1
        stop = 0
        print(HP)
        for elem in HP :
            if elem <= 0 :
                stop += 1
        if stop == 3 :
            return count
        
print(BFS(N,HP))