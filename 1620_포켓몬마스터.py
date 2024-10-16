import sys
input = sys.stdin.readline

N, M = map(int, input().split())
poketmon = {}
poketmonKey = {}
for i in range(1, N+1):
    temp = input().rstrip()
    poketmon[i] = str(temp)
    poketmonKey[temp] = i

for _ in range(M):
    temp = input().rstrip()

    if temp.isdigit():
        print(poketmon[int(temp)])
    else:
        print(poketmonKey.get(temp))
