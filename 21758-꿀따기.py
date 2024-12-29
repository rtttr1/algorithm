import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().split()))

prefix = [0]*N
prefix[0] = arr[0]
for i in range(1, N):
    prefix[i] = prefix[i-1] + arr[i]

middle = 0
for tong in range(1,N-1):
    sum,i,j = 0, 0, N-1
    sum += (prefix[tong]-prefix[i]+prefix[j-1]-prefix[tong-1])
    middle = max(middle, sum)

left = 0
for i in range(1,N-1):
    sum, tong, j = 0, 0, N-1
    sum += (prefix[i-1]+prefix[j-1]-arr[i])
    left = max(left, sum)

right = 0
for j in range(1,N-1):
    sum, tong, i = 0, N-1, 0
    sum += (prefix[tong]*2 - prefix[j] - prefix[i] - arr[j])
    right = max(sum, right)

print(max(left, middle, right))

# for tong in range(N):
#     for i in range(N-1):
#         if i == tong: continue
#         for j in range(i+1,N):
#             if j == tong: continue
#             sum = 0
#             if i < tong and j < tong:
#                 sum += (prefix[tong]*2 - prefix[j] - prefix[i] - arr[j])
#             elif i < tong and j > tong:
#                 sum += (prefix[tong]-prefix[i]+prefix[j-1]-prefix[tong-1])
#             else:
#                 sum += (prefix[i-1]-prefix[tong-1]*2+prefix[j-1]-arr[i])
#             answer = max(sum,answer)

# print(answer)

# def back(bees, tong, index):
#     if len(bees) == 2:
#         position[tong].append(bees.copy())
#         return
    
#     for i in range(index, N):
#         if i == tong:
#             continue
#         bees.append(i)
#         back(bees, tong, i+1)
#         bees.pop()
# temp = []
# for i in range(N):
#     back(temp, i, 0)
# answer = 0

# for i in range(N):
#     tong = i
#     for elem in position[i]:
#         bee1, bee2 = elem
#         temp = 0

#         if bee1 < tong and bee2 < tong:
#             temp += (sum(arr[bee2+1:tong+1])*2 + sum(arr[bee1+1:bee2]))
#         elif bee1 < tong and bee2 > tong:
#             temp += (sum(arr[bee1+1:tong+1]) + sum(arr[tong:bee2]))
#         else:
#             temp += (sum(arr[tong:bee1])*2 + sum(arr[bee1+1:bee2]))
#         answer = max(answer, temp)

# print(answer)