import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

arr.sort()

for elem in arr:
    print(elem[0], elem[1])
    