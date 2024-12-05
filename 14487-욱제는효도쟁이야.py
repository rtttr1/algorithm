import sys
input = sys.stdin.readline

n = int(input().rstrip())

v = list(map(int, input().split()))

v.sort()

print(sum(v[0:n-1]))