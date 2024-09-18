import sys
input = sys.stdin.readline

A, B = map(str, input().split())
A = list(map(int,A))
B = int(B)
max = [-1]
visited = [False] * len(A)

def back(C, visited): 
    if len(C) == len(A):
        if max[0] < int(''.join(str(s) for s in C)) < B and C[0] != 0:
            max[0] = int(''.join(str(s) for s in C))
        return
    
    for i in range(len(A)):
        if not visited[i]:
            C.append(A[i])
            visited[i] = True
            back(C, visited)
            C.pop()
            visited[i] = False

back([], visited)

print(max[0])