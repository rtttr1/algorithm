import sys
input = sys.stdin.readline

arr1 = list(map(str, input().rstrip()))
arr2 = list(map(str, input().rstrip()))
N, M = len(arr1), len(arr2)
dp = [0] * (M+1)
answer = 0   

# arr1
for i in range(1,N+1):
    temp = [0]*(M+1)
    #arr2
    for j in range(1,M+1):
        if arr1[i-1] == arr2[j-1]:
            temp[j] = 1 + dp[j-1]
            answer = max(temp[j], answer)
    dp = temp

print(answer)
