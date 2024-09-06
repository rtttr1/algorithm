import sys
input = sys.stdin.readline

S = input().rstrip()
q = int(input().rstrip())

count = [[0]*26]

for j in range(len(S)):
    count.append(count[len(count) - 1][:])
    count[j+1][ord(S[j])-97] += 1

result = []

for _ in range(q):
    ch, start, end = map(str, input().split(' '))
    result.append(count[int(end)+1][ord(ch)-97]-count[int(start)][ord(ch)-97])

for elem in result:
    print(elem)

