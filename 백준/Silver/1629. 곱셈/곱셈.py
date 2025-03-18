import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def fpow(a, b, c):
    if b == 1:
        return a % c
    
    # 쭉 타고 들어가며 분할을 먼저
    x = fpow(a, b//2, c)

    # 분할된 값으로 다시 올라가며 정복하기
    if b % 2 == 0:
        return (x*x) % c
    else:
        return (x*x*a) % c


print(fpow(A, B, C))