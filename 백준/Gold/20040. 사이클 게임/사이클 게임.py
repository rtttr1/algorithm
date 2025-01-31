import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr= []

for _ in range(m):
    arr.append(map(int,input().split()))
parents = [i for i in range(n)]

def get_parent(x):
    if parents[x] == x:
        return x
    
    parents[x] = get_parent(parents[x])
    return parents[x]

def same_parent(a,b):
    return get_parent(a) == get_parent(b)

def union_parent(a,b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b:
        parents[b]=a
    else:
        parents[a]=b

answer = 0
for i in range(m):
    a, b = arr[i]

    if same_parent(a,b):
        answer = i+1
        break

    union_parent(a,b)

print(answer)