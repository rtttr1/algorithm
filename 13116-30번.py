import sys

T = int(sys.stdin.readline().strip())
answer = []
for _ in range(T) :
    A, B = map(int, sys.stdin.readline().strip().split(' '))
    a, b = 0, 0
    for i in range(10) :
        if pow(2, i) <= A < pow(2, i+1) :
            a = i
        if pow(2, i) <= B < pow(2, i+1) :
            b = i
    