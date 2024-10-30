import sys
input = sys.stdin.readline
from collections import deque

A, B = map(int, input().split())

def BFS():
    queue = deque([[A, 0]])

    while queue:
        num, count = queue.popleft()

        if num == B:
            return count + 1
        
        temp = num*2

        if temp <= B:
            queue.append([temp, count+1])
        
        temp = int(str(num)+'1')
        
        if temp <= B:
            queue.append([temp, count+1])

    return -1

print(BFS())