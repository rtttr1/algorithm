import sys

input = sys.stdin.readline

N = int(input().rstrip())
arr = input().rstrip()

dp = [1]*21

for i in range(2,21):
    dp[i] = dp[i-1] + dp[i-2]

count = arr.count('long')

indexArr = [arr.find('long')]

while len(indexArr) < count:
    indexArr.append(arr.find('long', indexArr[-1]+1))

sum = 1
longArr = []

for i in range(1, len(indexArr)):
    if indexArr[i] - indexArr[i-1] == 4:
        sum += 1
    else :
        longArr.append(sum)
        sum = 1

if sum != 0 :
    longArr.append(sum)

answer = 1
for elem in longArr:
    answer *= dp[elem]

print(answer)