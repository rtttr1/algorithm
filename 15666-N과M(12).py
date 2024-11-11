import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

answerSet = set()

s = []

def Back(s, index, answerSet):
    # 탈출조건
    if len(s) == M:
        return answerSet.add(tuple(s))
    
    for i in range(index, N):
        s.append(arr[i])
        Back(s, i, answerSet)
        s.pop()
        
Back(s, 0, answerSet)

answer = list(answerSet)
answer.sort()
for elem in answer:
    print(' '.join(map(str, elem)))