import sys

N = int(sys.stdin.readline())
count = 0
for i in range(5, N + 1):
    check = i

    if check % 5 == 0:
        while check % 5 == 0:
            count += 1
            check = check / 5

print(count)
