import sys
input = sys.stdin.readline

word = str(input().rstrip())
temp = list(word)
temp.sort()

answer = []
point = 0
count = 0

for elem in temp:
    if count == 3:
        for i in range(len(word)-1, point-1, -1):
            answer.append(word[i])
        break

    index = word.find(elem, point)
    if index == -1:
        continue
    else:
        for i in range(index, point-1, -1):
            answer.append(word[i])
        point = index+1
        count += 1

print(''.join(answer))