import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
friend = list(map(int, input().split()))
answer = 0
for people in arr[:M]:
    if people not in friend:
        answer += 1

print(answer)