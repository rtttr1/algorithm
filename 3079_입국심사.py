import sys
input = sys.stdin.readline

N, M = map(int, input().split())
T = []
for _ in range(N):
    T.append(int(input().rstrip()))

T.sort()

def decision(mid, M, T):
    p = 0
    for elem in T:
        p += mid // elem
        if p >= M:
            return True
        elif mid // elem == 0:
            return False

def binary_search(M, T):
    low, high = 0, T[0]*M

    while low + 1 < high:
        mid = (low + high) // 2
        if decision(mid, M, T):
            high = mid
        else:
            low = mid

    return high

print(binary_search(M, T))