import sys
input = sys.stdin.readline

N = int(input().rstrip())

chatSet = set()
answer = 0

for i in range(N):
    chat = input().rstrip()
    
    if chat == 'ENTER':
        answer += len(chatSet)
        chatSet.clear()
    else:
        chatSet.add(chat)

answer += len(chatSet)
print(answer)