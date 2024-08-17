import sys

T = int(sys.stdin.readline())


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


for i in range(T):
    a, b = map(int, sys.stdin.readline().split())

    n = 0

    if a > b:
        n = gcd(a, b)
    else:
        n = gcd(a, b)

    print(int(a * b / n))
