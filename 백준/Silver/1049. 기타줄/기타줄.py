import sys
import math
input = sys.stdin.readline

N, M = map(int, input().split())
minSet, minOne = 10e9, 10e9

for _ in range(M):
    a, b = map(int, input().split())
    minSet, minOne = min(minSet, a), min(minOne, b)

if minOne*6 <= minSet:
    print(minOne*N)
else:
    answer = math.ceil(N / 6) * minSet
    answer = min(answer, math.floor(N / 6) * minSet +  minOne*(N - math.floor(N / 6)*6))
    print(answer)