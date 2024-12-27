import sys
input = sys.stdin.readline

n, k = map(int, input().split())

def back(n, list):
    if sum(list) == n:
        answers.append(list)
        return
    
    for elem in [1,2,3]:
        if sum(list) + elem <= n:
            list.append(elem)
            back(n, list.copy())
            list.pop()

temp = []
answers = []
back(n, temp)
if len(answers) < k:
    print(-1)
else:
    print('+'.join(map(str, answers[k-1])))