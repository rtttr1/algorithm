import sys
input = sys.stdin.readline

N = int(input().rstrip())

arr = [list(map(int, input().split())) for _ in range(N)]

def getTriangleArea(coor1, coor2, coor3):
    x1, y1 = coor1
    x2, y2 = coor2
    x3, y3 = coor3

    area = 0.5*(x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3)

    return  area

answer = 0
for i in range(1, N-1):
    answer += getTriangleArea(arr[0], arr[i], arr[i+1])

print(round(abs(answer), 1))