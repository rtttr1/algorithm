import sys
input = sys.stdin.readline

N, M = map(int, input().split())

noListen = {}
noSee = {}

answer = []

for _ in range(N):
    noListen[input().rstrip()] = True

for _ in range(M):
    noSee[input().rstrip()] = True

keyArr = noListen.keys()

for key in keyArr:
    if key in noSee:
        answer.append(key)

print(len(answer))
answer.sort()
for elem in answer:
    print(elem)