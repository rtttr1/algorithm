import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))
visited = [False] * N
arr.sort()
stack = []
s = []

def Back(s, visited, stack):
    # 탈출조건
    if len(s) == M:
        return stack.append(s.copy())
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            s.append(arr[i])
            if s not in stack:
                Back(s, visited, stack)
            visited[i] = False
            s.pop()

Back(s, visited, stack)

for elem in stack:
    print(' '.join(map(str, elem)))
