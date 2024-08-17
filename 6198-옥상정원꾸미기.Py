import sys

N = int(sys.stdin.readline().strip())

hArr = []
stack = []
for i in range(N) :
    hArr.append(int(sys.stdin.readline().strip()))

sum = 0
for i in hArr :
    while stack and stack[-1] <= i :
        stack.pop()
    stack.append(i)

    sum += len(stack) - 1

print(sum)