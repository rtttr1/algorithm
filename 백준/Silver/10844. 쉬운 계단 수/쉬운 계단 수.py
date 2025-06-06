import sys
input = sys.stdin.readline

N = int(input().rstrip())

if N == 1:
    print(9)
else:
    dp = [[0]*(10) for _ in range(N)]
    dp[0] = [0,1,1,1,1,1,1,1,1,1]


    for i in range(1,N):
        for j in range(10):
            if j == 0: 
                dp[i][j] = dp[i-1][j+1]
            elif j == 9:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

    print(sum(dp[-1]) % 1000000000)