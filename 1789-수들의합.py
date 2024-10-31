import sys
input = sys.stdin.readline

S = int(input().rstrip())

count = 0
temp = 0
for i in range(1, S):
    if i + temp > S:
        break

    count += 1
    temp += i

if S == 1:
    print(1)
else:
    print(count)