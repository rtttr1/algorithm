import sys
from collections import deque 

N = int(sys.stdin.readline().strip())
inQueue = deque([])
out = []
count = 0

for i in range(N) :
    inQueue.append(sys.stdin.readline().strip())

for i in range(N) :
    out.append(sys.stdin.readline().strip())

for car in out :
    if car != inQueue[0]  :
        count += 1
        inQueue.remove(car)
    else :
        inQueue.popleft()

print(count)


