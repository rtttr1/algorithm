import sys
input = sys.stdin.readline

n = int(input()) 
taste_nums = list(map(int, input().split())) 
k = int(input()) 

step = n // k
for i in range(step, n + 1, step):
    print(*sorted(taste_nums[i - step : i]), end=' ')