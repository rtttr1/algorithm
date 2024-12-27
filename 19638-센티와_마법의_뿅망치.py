import sys
input = sys.stdin.readline
import heapq 

N, H, T = map(int, input().split())
heap = []

for _ in range(N):
    num = int(input().rstrip())
    heapq.heappush(heap, (-num, num))

count = 0

for _ in range(T):
    num = heapq.heappop(heap)[1] 
    if num < H or num == 1:
        heapq.heappush(heap, (-num, num))
        break
    
    num = num // 2
    heapq.heappush(heap, (-num, num))
    count += 1

num = heapq.heappop(heap)[1]
if num < H:
    print('YES')
    print(count)
else:
    print('NO')
    print(num)
