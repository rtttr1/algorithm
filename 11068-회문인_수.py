import sys
input = sys.stdin.readline

T = int(input().rstrip())

def convert(n, b):
    T = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz#$"
    q, r = divmod(n, b)
    if q == 0:
        return T[r]
    else:
        return convert(q, b) + T[r]

for _ in range(T):
    num = int(input().rstrip())
    answer = 0

    for j in range(2, 65):
        temp = convert(num, j)
        if temp == temp[::-1]:
            answer = 1
            break
    print(answer)