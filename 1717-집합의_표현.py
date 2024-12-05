import sys 
input = sys.stdin.readline

# 재귀 한도 늘려주기
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())

parent = [i for i in range(n+1)]

# 같은 부모 찾기
def same_parent(a, b):
    return get_parent(a) == get_parent(b)

# 부모 합치기
def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 부모 찾기
def get_parent(x):
    if parent[x] == x: return x
    parent[x] = get_parent(parent[x])
    return parent[x]


for _ in range(m):
    cal, a, b = map(int, input().split())

    if cal == 0:
        union_parent(a,b)
    else:
        if same_parent(a, b):
            print('yes')
        else:
            print('no')
