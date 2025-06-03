import sys
input = sys.stdin.readline

T = int(input().rstrip())

for i in range(T):
    stack = []
    arr = list(input().rstrip())
    flag = True

    for j in range(len(arr)):
        if arr[j] == '(':
            stack.append(arr[j])
        else:
            if len(stack) == 0:
                flag = False
                break
            stack.pop()

    if len(stack) != 0:
        flag = False
    
    if flag:
        print('YES')
    else:
        print('NO')


