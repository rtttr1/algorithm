import sys
import copy
# 깊은복사 조심!!!!!!!
temp = list(sys.stdin.readline().strip())
middle = copy.deepcopy(temp)

operator = ["-", "+", "*", "/"]
stack1 = []  # 알파벳 넣기
stack2 = []  # 연산자 넣기
stack3 = []  # 빼낸거 넣기
i = 0

for el in temp:
    if middle[i] == ")":
        i += 1
    if el == "*" or el == "/":
        if (middle[i - 1] != ")") and (middle[i + 1] != "("):
            # print("삽입하러 들어옴!")
            middle.insert(i + 2, ")")
            middle.insert(i - 1, "(")
            i += 1
    # print("temp=", temp)
    # print("el=", el, "i=", i, middle)
    i += 1


middle.insert(0, "(")
middle.append(")")
print("middle=", middle)

for i in range(len(middle)):
    if middle[i] == ")":
        stack3.append(stack2.pop())
        while True:
            el = stack1.pop()
            if el == "(":
                break
            else:
                stack3.append(el)
        while len(stack3) != 0:
            stack1.append(stack3.pop())

    elif middle[i] not in operator:
        stack1.append(middle[i])

    elif middle[i] in operator:
        stack2.append(middle[i])

print("stack1=", stack1)
for el in stack1:
    print(el, end="")
