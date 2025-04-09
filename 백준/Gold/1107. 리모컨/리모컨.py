import sys
input = sys.stdin.readline

N = str(input().rstrip())
M = int(input().rstrip())

# 고장난 버튼이 없는 경우
if M == 0:
    print(min(len(N), abs(int(N)-100)))

# 고장난 버튼이 있는 경우
else:
    arr = set(map(int,input().split()))
    btns = list(set(i for i in range(10))-arr)

    def back(s):
        global answer
        
        # 각 경우마다 최소값 최신화
        if len(s) != 0:
            num = int(''.join(map(str,s)))
            answer = min(answer, abs(int(N)-num) + len(str(num)))
        
        # 6자리가 안되는 경우 버튼 추가
        if len(s) < 6:
            for num in btns:
                s.append(num)
                back(s)
                s.pop()

    temp = []
    answer = abs(int(N)-100)
    back(temp)
    print(answer)