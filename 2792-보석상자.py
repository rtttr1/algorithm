import sys
import math
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []

for _ in range(M):
    arr.append(int(input().rstrip()))

def binary_search(max):
    low, high = 1, max
    
    while low < high:
        mid = (low + high) // 2

        if decision(mid):
            high = mid 
        else:
            low = mid + 1
        
    return low

def decision(max):
    count = 0
    for elem in arr:
        if elem > max:
            count += math.ceil(elem / max)
        else:
            count += 1
    
    if count > N:
        return False
    else:
        return True
    
print(binary_search(max(arr)))
