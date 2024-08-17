import sys 

N = int(sys.stdin.readline().strip())

arr = [list(map(int, input().split())) for _ in range(N)]

if N == 2 :
    print(1, 1)
else :
    arr[0][0] = (arr[0][1] + arr[0][2] - arr[1][2]) // 2 
    for i in range(1, N) :
        arr[0][i] = arr[0][i] - arr[0][0]

    for i in arr[0] :
        print(i, end = ' ')
        