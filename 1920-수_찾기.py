import sys
input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().split()))
M = int(input().rstrip())
Marr = list(map(int, input().split()))
A.sort()

def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return 1
        elif data[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for elem in Marr:
    print(binary_search(elem, A))