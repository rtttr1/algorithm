import sys

N, M = map(int, sys.stdin.readline().strip().split(' '))

arr = list(map(int, input().split()))

section = []

for i in range(M) :
    x, y = map(int, sys.stdin.readline().strip().split(' '))
    section.append([x,y])

sumArr = []
sum = 0
for i in arr :
    sumArr.append(sum)
    sum += i
sumArr.append(sum)
for points in section :
    print(sumArr[points[1]]-sumArr[points[0]-1])