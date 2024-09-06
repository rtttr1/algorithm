import sys
input = sys.stdin.readline

n = int(input().strip())
xArr = []
yArr = []

for _ in range(n):
    x, y = map(int, input().split())
    xArr.append(x)
    yArr.append(y)

xArr.sort()
yArr.sort()

X = xArr[len(xArr)//2]
Y = yArr[len(yArr)//2]

sum = 0
for i in range(n):
    sum += (abs(xArr[i] - X) + abs(yArr[i] - Y))
print(sum)