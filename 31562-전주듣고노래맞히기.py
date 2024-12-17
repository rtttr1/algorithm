import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dict = {}
for _ in range(N):
    elem = list(map(str, input().split()))

    T = int(elem[0])
    S = str(elem[1])
    arr = ''.join(elem[2:5])

    if arr not in dict:
        dict[arr] = S
    else:
        dict[arr] = '?'

for _ in range(M):
    arr = ''.join(list(map(str, input().split())))

    if arr in dict:
        print(dict[arr])
    else:
        print('!')
                  
