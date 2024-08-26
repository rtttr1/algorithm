import sys
from queue import PriorityQueue

N = int(sys.stdin.readline().strip())

queue = PriorityQueue(maxsize=100000)
num = []

for _ in range(N) :
    num.append(int(sys.stdin.readline().strip()))

for elem in num :
    if elem == 0 :
        if queue.empty():
            print(0)
        else :
            print(queue.get())
    else :
        queue.put(elem)

