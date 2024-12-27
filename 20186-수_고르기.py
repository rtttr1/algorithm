import sys
input = sys.stdin.readline
A, B = map(int, input().split())
print((A+B)*(A-B))
N, K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
answer = sum(arr[0:K])

for i in range(1,K):
    answer += -1*i

print(answer)



