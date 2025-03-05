import sys 
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T): 
    n,k,t,m = map(int, input().split())
    scores = [[0]*(k+1) for _ in range(n+1)]
    count = [0]*(n+1)
    last = [0]*(n+1)
    for k in range(m):
        i,j,s = map(int, input().split())
        scores[i][j] = max(scores[i][j], s)
        count[i] += 1
        last[i] = k

    arr = []
    for i in range(1, n+1):
        arr.append([sum(scores[i]), count[i], last[i], i])
    
    arr.sort(key = lambda x: (x[0], -x[1], -x[2]),reverse=True)
    for i in range(n):
        if arr[i][-1] == t:
            print(i+1)