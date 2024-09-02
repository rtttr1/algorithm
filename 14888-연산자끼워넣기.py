import sys

N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split(' ')))
tool = list(map(int, sys.stdin.readline().strip().split(' ')))

answer = []

def count(i, num, result):
    if i == 0:
        return result + num
    elif i == 1:
        return result - num
    elif i == 2:
        return result * num
    elif i == 3:
        if result < 0 :
            return (-1 * result // num) * -1
        else :
            return result // num

def DFS(index, result, tool, arr) :
    if index == N :
        answer.append(result)
    else :
        for i in range(4) :
            if tool[i] > 0 :
                tool[i] -= 1
                DFS(index+1, count(i, arr[index], result), tool, arr)
                tool[i] += 1

DFS(1, arr[0], tool, arr)
print(max(answer))
print(min(answer))