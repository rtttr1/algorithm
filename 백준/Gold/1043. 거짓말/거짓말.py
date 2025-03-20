import sys
input = sys.stdin.readline

N, M = map(int, input().split())

knows = list(map(int, input().split()))[1:]
answer = 0
arr = [list(map(int, input().split()))[1:] for _ in range(M)]
parent = [i for i in range(N+1)]

def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]

def same_parent(a,b):
    return get_parent(a) == get_parent(b)

def union_parent(a,b):
    a = get_parent(a)
    b = get_parent(b)

    if a in knows and b in knows: return
    elif a in knows and b not in knows:
        parent[b] = a
    elif a not in knows and b in knows:
        parent[a] = b
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b 

arr.sort(key = lambda x: len(x), reverse=True)

for elem in arr:
    if len(elem) == 0: 
        continue 
    
    for i in range(len(elem)-1):
        union_parent(elem[i], elem[i+1])

for elem in arr:
    isKnow = False
    for people in elem:
        if get_parent(people) in knows:
            isKnow = True
            break
    if not isKnow:
        answer += 1

print(answer)
