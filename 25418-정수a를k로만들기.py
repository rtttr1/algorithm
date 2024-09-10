import sys
from collections import deque
input = sys.stdin.readline

A, K = map(int, input().split())

dp = [0]*(K+1)

for elem in range(A,K):
    if elem + 1 <= K and dp[elem+1] == 0:
        dp[elem+1] = dp[elem]+1
    if elem*2 <= K and dp[elem*2] == 0:
        dp[elem*2] = dp[elem]+1

print(dp[K]) 



# visited = [False]*(K*2+1)

# def BFS(A, K) :
#     queue = deque([[A,0]])
#     visited[A] = True

#     while queue :
#         node, count = queue.popleft()

#         if node == K :
#             return count
        
#         for elem in [node+1, node*2]:
#             if elem <= K and not visited[elem]:
#                 queue.append([elem, count+1])
#                 visited[elem] = True

# print(BFS(A, K))





