import sys
input = sys.stdin.readline

S = str(input().rstrip())
temp = [S[0]]

for i in range(1, len(S)):
    if temp[-1] == S[i]:
        continue

    temp.append(S[i])

print(min(temp.count('0'), temp.count('1')))
    