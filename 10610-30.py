import sys 

N = list(map(int,sys.stdin.readline().strip()))

N.sort(reverse=True)
N = int(''.join(map(str, N)))

if N % 30 == 0 :
    print(N)
else :
    print(-1)