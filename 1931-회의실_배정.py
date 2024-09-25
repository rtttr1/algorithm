import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

arr = sorted(arr, key=lambda x:(x[1], x[0]))
answer = 0

end = 0
for elem in arr:
    if elem[0] >= end :
        answer += 1
        end = elem[1]
print(answer)