s = list(input())

stack = []
ans = 0

for i in range(len(s)):
    if s[i] == "(":
        stack.append(s[i])
    elif s[i] == ")":
        stack.pop()

        if s[i - 1] == "(":
            ans += len(stack)
        else:
            ans += 1
print(ans)
