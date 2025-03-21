import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))

def decision(target):
    count = 1
    sum = 0
    for elem in arr:
        if sum + elem > target:
            count += 1
            sum = elem
        else:
            sum += elem
    
    if count <= M:
        return False
    else:
        return True

def binary_search():
    low = max(arr) - 1
    high = sum(arr)

    while low + 1 < high:
        mid = (low + high) // 2
      
        if decision(mid):
            low = mid
        else:
            high = mid
    
    return high

print(binary_search())