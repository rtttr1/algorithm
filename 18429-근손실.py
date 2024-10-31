import sys
input = sys.stdin.readline
from itertools import permutations

N, K = map(int, input().split())
A = list(map(int,input().split()))

def check(arr, sum = 500):
    for elem in arr:
        sum += (elem - K)

        if sum < 500:
            return False
    return True

nums = list(permutations(A, N))

answer = 0
for elem in nums:
    if check(elem):
        answer += 1
print(answer)
