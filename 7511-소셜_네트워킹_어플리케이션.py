import sys
input = sys.stdin.readline

T = int(input().rstrip())

def same_parent(a, b):
    return find_parent(a) == find_parent(b)

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for t in range(1,T+1):
    print("Scenario %s:" % t)
    N = int(input().rstrip())
    K = int(input().rstrip())
    
    parent = [i for i in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        if not same_parent(a,b):
            union(a,b)
    
    M = int(input().rstrip())
    for _ in range(M):
        u, v = map(int, input().split())
        if same_parent(u,v):
            print(1)
        else:
            print(0)
    print()

    