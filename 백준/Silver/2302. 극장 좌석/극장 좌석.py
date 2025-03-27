import sys
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())

fix = [int(input().rstrip()) for _ in range(M)]

if N == 1:
    print(1)
else:
    dp = [1]*(N+1)
    dp[1] = 1

    for i in range(2, N+1):
        dp[i] = dp[i-1] + dp[i-2]
    if M == 0:
        print(dp[-1])
    else:
        answer = 1
        for i in range(M):
            if i == 0:
                answer *= dp[fix[i]-1]
            else:
                answer *= dp[fix[i] - fix[i-1]-1]

        answer *= dp[N-fix[-1]]
        print(answer)

