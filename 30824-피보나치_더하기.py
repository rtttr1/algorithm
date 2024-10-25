import sys
input = sys.stdin.readline

T = int(input().rstrip())
        
def two(fibo, x): 
    for i in range(len(fibo)):
        for j in range(len(fibo)):
            if fibo[i] + fibo[j] == x:
                return 'YES'
    return 'NO'
                
def three(fibo, x):
    for i in range(len(fibo)):
        for j in range(len(fibo)):
            for k in range(len(fibo)): 
                if fibo[i] + fibo[j] + fibo[k] == x:
                    return 'YES'
    return 'NO'

for _ in range(T):
    k, x = map(int, input().split())

    fibo = [1,1]
    while fibo[-1] < x:
        fibo.append(fibo[-1] + fibo[-2])

    if k == 1:
        if x in fibo:
            print('YES')
        else:
            print('NO')
    elif k == 2:
        print(two(fibo, x))
    elif k == 3:
        print(three(fibo, x))

