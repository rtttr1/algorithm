import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

V, E = map(int, input().split())
edges = []
parent = [i for i in range(V+1)]

for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((A,B,C))

edges.sort(key= lambda x:x[2])

# 부모를 찾아주는 함수
def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]

# 같은 부모를 가졌는지 여부를 확인하는 함수
def same_parent(a,b):
    return get_parent(a) == get_parent(b)

# 부모를 통일시켜주는 함수
def union_parent(a,b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

answer = 0
for a,b,c in edges:
    if not same_parent(a,b):
        union_parent(a,b)
        answer += c
        
print(answer)
