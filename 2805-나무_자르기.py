import sys
input = sys.stdin.readline

N, M = map(int, input().split())

trees = list(map(int, input().split()))

def decision(arr, mid, M):
    sum = 0
    for elem in arr :
        if elem > mid :
            sum += (elem - mid)

    return M <= sum

def binary_search(trees, N, M):
    low = 0
    high = max(trees)

    while low + 1 < high :
        mid = (low + high) // 2
        
        if decision(trees, mid, M) :
            low = mid
        else :
            high = mid

    return low

print(binary_search(trees, N, M))




