from collections import deque

N, K = map(int, input().split())
q = deque()

for i in range(1, N + 1):
    q.append(i)

ans = []

for i in range(N):
    for i in range(K - 1):
        q.append(q.popleft())
    ans.append(q.popleft())

print("<" + ", ".join(map(str, ans)) + ">")
