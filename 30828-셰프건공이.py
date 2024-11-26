import sys 
input = sys.stdin.readline

N = int(input().rstrip())
T = list(map(int, input().split()))
Q = int(input().rstrip())

for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    dp = [[0]*(r-l+1) for _ in range(r-l+1)]
    temp = T[l:r+1]
    
    for i in range(r-l+1):
        for j in range()


# DP or Back트래킹
# 하나씩 해봐야함 아무래도 DP인듯?

# log(N)