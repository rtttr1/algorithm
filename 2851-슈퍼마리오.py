import sys
input = sys.stdin.readline

arr = [int(input().rstrip()) for _ in range(10)]

answer = 0

for i in range(10):
    if answer+arr[i] >= 100:
        if 100 - answer < answer+arr[i]-100:
            print(answer)
        else:
            print(answer+arr[i])
        exit()
    else:
        answer += arr[i]

print(answer)