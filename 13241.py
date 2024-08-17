import sys

T = int(sys.stdin.readline())

def gcd(a,b) :
    while b > 0:
        a , b = b, a % b
    return a

def lcd(a,b) :
    return a * b / gcd(a,b)

answer = []

for i in range(T) : 
    M, N = map(int, sys.stdin.readline().split())
    answer.append(int(lcd(M,N)))

for i in answer : 
    print(i)