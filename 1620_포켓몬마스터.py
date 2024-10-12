import sys
input = sys.stdin.readline

N, M = map(int, input().split())
poketmon = []

for _ in range(N):
    poketmon.append(str(input().rstrip()))

for _ in range(M):
    temp = input().rstrip()
    
    if isinstance(temp, int):
        print(poketmon[temp-1])
    else:
        print(poketmon.index(temp)+1)
