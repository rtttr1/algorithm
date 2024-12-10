import sys 
input = sys.stdin.readline

sdocu = [list(map(int, input().rstrip())) for _ in range(9)]

def kan(x,y,n):
    a, b = x // 3, y // 3

    for i in range(3*a, 3*a+3):
        for j in range(3*b, 3*b+3):
            if sdocu[i][j] == n:
                return False
    return True

def sero(y,n):
    for i in range(9):
        if sdocu[i][y] == n:
            return False
    return True

def solveSdocu(index):
    # 반환 조건
    if index == len(arr): 
        for i in range(9):
            print(''.join(map(str,sdocu[i])))
        exit()
    
    # 값 넣을 좌표
    x, y = arr[index][0], arr[index][1]

    # sdocu 해결
    for i in range(1,10):
        # 해당 숫자가 들어갈 수 있는지 체크
        if i not in sdocu[x] and kan(x,y,i) and sero(y,i):
            sdocu[x][y] = i
            solveSdocu(index+1)
            sdocu[x][y] = 0

arr = []
for i in range(9):
    for j in range(9):
        if sdocu[i][j] == 0:
            arr.append([i,j])

solveSdocu(0)