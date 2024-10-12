import sys
input = sys.stdin.readline

N, K, A, B = map(int, input().split())

plants = [K]*N
count = 0
while 0 not in plants:
    count += 1
    index = plants.index(min(plants))
    for i in range(index, index+A):
        plants[i] += B
    for i in range(N):
        plants[i] -= 1

print(count)