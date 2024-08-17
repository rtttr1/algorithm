import sys

N = sys.stdin.readline()
S = list(sys.stdin.readline().strip())

stack = []

for i in range(len(S)):
    if S[i] == "+":
        a = stack.pop()
        b = stack.pop()
        stack.append(a + b)
    elif S[i] == "-":
        b = stack.pop()
        a = stack.pop()
        stack.append(a - b)
    elif S[i] == "*":
        b = stack.pop()
        a = stack.pop()
        stack.append(a * b)
    elif S[i] == "/":
        b = stack.pop()
        a = stack.pop()
        stack.append(a / b)
    else:
        el = float(sys.stdin.readline())
        stack.append(el)

print("%.2f" % stack.pop())
