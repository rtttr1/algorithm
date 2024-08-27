import sys 

arr = list(map(int, sys.stdin.readline().strip().split(' ')))

sum = 0
for i in arr :
    sum += pow(i, 2)

print(sum % 10)