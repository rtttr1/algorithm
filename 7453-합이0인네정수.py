import sys
input = sys.stdin.readline

n = int(input().rstrip())
A = []
B = []
C = []
D = []
AB = []
CD = []

for i in range(n) :
    arr = list(map(int, input().split(' ')))
    A.append(arr[0])
    B.append(arr[1])
    C.append(arr[2])
    D.append(arr[3])

for i in range(n):
    for j in range(n):
        AB.append(A[i] + B[j])
        CD.append(C[i] + D[j])

AB.sort()
CD.sort()

def upper(start, end, arr, target):
    while start < end :
        mid = (start+end) // 2
        if arr[mid] <= target: start = mid + 1
        else: end = mid
    return start
            
def lower(start, end, arr, target):
    while start < end:
        mid = (start+end) // 2
        if arr[mid] < target: start = mid + 1
        else: end = mid
    return start

answer = 0
for i in range(n*n):
    up = upper(0, len(AB)-1, AB, -CD[i])
    low = lower(0, len(AB)-1, AB, -CD[i])
    answer +=  (up - low)

print(answer)