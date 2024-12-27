import sys
input = sys.stdin.readline

N, M = map(int, input().split())

parent = [i for i in range(N+1)]

def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x]) # get_parent 거슬러 올라가면서 parent[x] 값도 갱신
    return parent[x]

def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b: # 작은 쪽이 부모가 된다. (한 집합 관계라서 부모가 따로 있는 건 아님)
        parent[b] = a
    else:
        parent[a] = b        

def same_parent(a, b):
    return get_parent(a) == get_parent(b)

edges = []
for _ in range(M):
    A,B,C = map(int, input().split())
    edges.append([A,B,C])

edges.sort(key=lambda x:x[2])

costs = []

for a,b,cost in edges:
    if not same_parent(a,b):
        union_parent(a,b)
        costs.append(cost)
    
costs.sort(reverse=True)
print(sum(costs[1:]))
