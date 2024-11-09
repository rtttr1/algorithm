import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
visited = [False]*N

def back(stack, visited):
    # 반환 조건
    if len(stack) == M:
        return print(' '.join(map(str, stack)))
        
    for i in range(N):
        # 방문해도 되는 노드면
        if visited[i] == False:
            # 방문하기
            visited[i] = True
            stack.append(arr[i])
            back(stack, visited)
            # 부모노드로 돌아가기
            stack.pop()
            visited[i] = False

s = []
back(s, visited) 