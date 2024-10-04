import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    nums = list(map(int, input().split()))
    nums[8] = nums[8] + nums[5]
    nums[5] = 0
    answer = []
    i = 8
    while i > -1:
        if nums[i]:
            nums[i] -= 1
            answer.append(i+1)
        elif not nums[i]:
            i -= 1
    
    for i in range(0, len(answer), +2):
        print(answer[i], end=' ')
    if len(answer) % 2 == 0:
        for j in range(len(answer)-1, 0, -2):
            print(answer[j], end=' ')
    else: 
        for j in range(len(answer)-2, 0, -2):
            print(answer[j], end=' ')
    print()
    
    