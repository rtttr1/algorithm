import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))
visited = [False] * N
# arr.sort()
answerSet = set()

s = []

def Back(s, visited, answerSet):
    # 탈출조건
    if len(s) == M:
        return answerSet.add(tuple(s))
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            s.append(arr[i])
            Back(s, visited, answerSet)
            visited[i] = False
            s.pop()

Back(s, visited, answerSet)
answer = list(answerSet)
answer.sort()
for elem in answer:
    print(' '.join(map(str, elem)))
