import sys
input = sys.stdin.readline

D, K = map(int, input().split())


for i in range(1, K+1):
    dp = [K, K-i]

    while len(dp) < D:
        if dp[-1] >= dp[-2] - dp[-1] :
            dp.append(dp[-2] - dp[-1])
        else:
            break
    
    if len(dp) == D and dp[-1] != 0:
        print(dp[-1])
        print(dp[-2])
        break
