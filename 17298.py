N = int(input())
A = list(map(int, input().split()))


ans = [-1] * N
stack = []
stack.append(0)

for i in range(1, N):
    while stack and A[i] > A[stack[-1]]:
        ans[stack[-1]] = A[i]
        stack.pop()
    stack.append(i)

for el in stack:
    ans[el] = -1

for el in ans:
    print(el, end=" ")
