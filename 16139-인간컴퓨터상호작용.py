import sys
input = sys.stdin.readline

S = input().rstrip()
q = int(input().rstrip())

count = [[0 for _ in range(len(S)+1)] for _ in range(26)]


for j in range(len(S)):
    num = count[ord(S[j])-97][j+1]+1
    count[ord(S[j])-97][j+1:] = [num]*(len(S)-j)
    
result = []

for _ in range(q):
    ch, start, end = map(str, input().split(' '))
    result.append(count[ord(ch)-97][int(end)+1]-count[ord(ch)-97][int(start)])

for elem in result:
    print(elem)

