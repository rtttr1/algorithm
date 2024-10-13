import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().split()))
LIS = [arr[0]]

def binary_search(last):
    low = 0
    high = len(LIS) - 1

    while low <= high:
        mid = (low + high) // 2
    
        if LIS[mid] == last: 
            return mid
        elif LIS[mid] < last:
            low = mid + 1
        else:
            high = mid - 1

    return low

for i in range(N):
    if arr[i] > LIS[-1]:
        LIS.append(arr[i])
    else:
        index = binary_search(arr[i])
        LIS[index] = arr[i]

print(len(LIS))
