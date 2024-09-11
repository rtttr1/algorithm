import sys

input = sys.stdin.readline

N = int(input().rstrip())

for _ in range(N):
    quiz = map(str, input().rstrip())
    sum = 0
    count = 0
    for elem in quiz:
        if elem == 'O':
            count += 1
            sum += count
        elif elem == 'X':
            count = 0
    print(sum)
    