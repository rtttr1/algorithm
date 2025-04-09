import sys
input = sys.stdin.readline

N = str(input().rstrip())
M = int(input().rstrip())

if M == 0:
    print(min(len(N), abs(int(N)-100)))
else:
    arr = set(map(int,input().split()))
    btns = list(set(i for i in range(10))-arr)

    def back(s):
        global answer
        
        if len(s) != 0:
            num = int(''.join(map(str,s)))
            answer = min(answer, abs(int(N)-num) + len(str(num)))
            
        if len(s) < 6:
            for num in btns:
                s.append(num)
                back(s)
                s.pop()

    temp = []
    answer = abs(int(N)-100)
    back(temp)
    print(answer)