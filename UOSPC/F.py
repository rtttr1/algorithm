import sys
input = sys.stdin.readline

X, Y, D = map(int, input().split())
N = int(input().rstrip())
product = []

for _ in range(N):
    product.append(list(map(int,input().split())))
    