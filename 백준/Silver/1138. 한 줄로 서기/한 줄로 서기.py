import sys 
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().split()))
temp = []

def check(s, i):
    if len(s) == 0:
        return 0
    
    count = 0
    for j in range(len(s)):
        if s[j] > i:
            count += 1
    return count

def back(s):
    if len(s) == N: 
        temp.append(s.copy())
        return
    
    for i in range(N):
        if i not in s:
            if len(s) == 0:
                if arr[i] == 0:
                    s.append(i)
                    back(s)
                    s.pop()
            elif check(s, i) == arr[i]:  
                s.append(i)
                back(s)
                s.pop()

temp1 = []
back(temp1)
for i in temp[0]:
    print(i+1, end = ' ')

