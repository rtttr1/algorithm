import sys

T = int(sys.stdin.readline().strip())

money = [25, 10, 5, 1]
arr = []

for _ in range(T) :
    arr.append(int(sys.stdin.readline().strip()))

result = []
for i in arr :
    temp = i
    tempArr = []
    for j in money :
        count = 0
        while temp - j >= 0 :
            temp -= j
            count += 1
        tempArr.append(count)
    result.append(tempArr)
    
for elem in result :
    for j in elem:
        print(j, end= ' ')
    print()