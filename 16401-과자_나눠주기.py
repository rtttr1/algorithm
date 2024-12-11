import sys
input = sys.stdin.readline

M, N = map(int, input().split())

L = list(map(int, input().split()))

L.sort()

def decision(snacks, mid):
    count = 0
    for snack in snacks:
        count += snack // mid
    if count >= M:
        return True
    else:
        return False

answer = 0


low = 1
high = L[N-1]

while low <= high :
    mid = (low + high) // 2
        
    if decision(L, mid) :
        low = mid + 1
        answer = mid
    else :
        high = mid - 1

print(answer)