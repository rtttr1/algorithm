import sys
from collections import Counter

N = int(sys.stdin.readline().strip())
arr = []

for i in range(N) :
    arr.append(int(sys.stdin.readline().strip()))

arr.sort()

sum = 0
for i in arr :
    sum += i

average = round(sum / N)
middle = arr[N//2]

range = arr[N-1] - arr[0]

num = Counter(arr).most_common(2)

if len(num) > 1 :
    if num[0][1] == num[1][1]:
        lot = num[1][0]
    else: 
        lot = num[0][0]
else :
    lot = num[0][0]

print(average)
print(middle)
print(lot)
print(range)