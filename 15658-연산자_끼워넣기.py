import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().split()))
symbolNum = list(map(int, input().split()))
answer = [-1000000000, 1000000000]

def calculate(num1, num2, symbol):
    if symbol == 0: return num1 + num2
    elif symbol == 1: return num1 - num2 
    elif symbol == 2: return num1 * num2
    elif symbol == 3:
        return ((-1*num1) // num2) * (-1) if num1 < 0 else num1 // num2

def back(index, result):
    if index == N-1:
        if result > answer[0]: answer[0] = result
        if result < answer[1]: answer[1] = result
        return
    
    for i in range(4):
        if symbolNum[i] > 0:
            symbolNum[i] -= 1
            back(index+1, calculate(result, arr[index+1], i))
            symbolNum[i] += 1

back(0, arr[0])

print(answer[0])
print(answer[1])
