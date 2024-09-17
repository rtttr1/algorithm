import sys
input = sys.stdin.readline

N, M = map(int, input().split())

book = [[0,0]]

dp = [[0]*(N+1) for _ in range(M+1)]

for _ in range(M):
    book.append(list(map(int, input().split())))
book = sorted(book)

for i in range(1, M+1):
    for j in range(1, N+1):
        day, page = book[i][0], book[i][1]
        if j < day:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-day] + page)


print(dp[M][N])