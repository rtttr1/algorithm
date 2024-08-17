import sys

arr = []

while True : 
    T = int(sys.stdin.readline().strip())
    if T == 0 :
        break
    else :
        arr.append(T)

n = max(arr)*2

primeArr = [False, False] + [True for i in range(n-1)]

for i in range(2, n+1) :
    if not primeArr[i] :
        continue
    for j in range(i*2, n+1, +i) :
        primeArr[j] = False


for i in arr :
    count = 0
    for j in range(i+1, i*2+1) :
        if primeArr[j] == True:
            count +=1
    print(count)
    
        
