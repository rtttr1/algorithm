N = int(input())
A = list(map(int, input().split()))

stack1 = []
stack2 = []


ans = []

for i in range(0, N):
    if len(stack1) == 0:
        stack1.append(A[i])
    # stack의 마지막값이 배열의 값보다 작은경우
    elif stack1[-1] < A[i]:
        while stack1[-1] < A[i]:
            stack1.pop()
            stack2.append(A[i])
            if len(stack1) == 0:
                break
        stack1.append(A[i])
        if i == N - 1 and len(stack1) != 1:
            stack2.append(-1)
        while len(stack2) != 0:
            ans.append(stack2.pop())
    else:
        stack1.append(A[i])


ans.append(-1)

for el in ans:
    print(el, end=" ")
