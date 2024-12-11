import sys
input = sys.stdin.readline

M, N = map(int, input().split())
sum = [1]*(2*M-1)

for day in range(N):
    a,b,c = map(int, input().split())
    for i in range(a, a+b):
        sum[i] += 1
    for i in range(a+b, a+b+c):
        sum[i] += 2

for i in range(M):
    print(' '.join(map(str, sum[M-i-1:M-i]+sum[M:])))


# 83점 풀이

# import sys
# input = sys.stdin.readline

# M, N = map(int, input().split())
# arr = []
# graph = [[1]*M for _ in range(M)]

# for _ in range(N):
#     count = list(map(int, input().split()))
#     temp = [0]*count[0]+[1]*count[1]+[2]*count[2]
#     arr.append(temp)

# graph = [[1]*M for _ in range(M)]

# for day in range(N):
#     for i in range(2*M-1):
#         if i < M:
#             graph[M-i-1][0] += arr[day][i]
#         else:
#             graph[0][i-M+1] += arr[day][i]

# for i in range(1,M):
#     for j in range(1,M):
#         graph[j][i] = graph[0][i]

# for elem in graph:
#     print(' '.join(map(str, elem)))