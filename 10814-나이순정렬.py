import sys

N = int(sys.stdin.readline())

arr = []
for i in range(N):
    age, name = sys.stdin.readline().strip().split(' ')
    arr.append([int(age), name])

sortedArr = sorted(arr, key= lambda arr: arr[0])

for i in sortedArr :
    print(i[0], i[1])
