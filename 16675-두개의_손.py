import sys
input = sys.stdin.readline

arr = list(map(str, input().split()))

RSP = {
    'R': 'S',
    'P': 'R',
    'S': 'P'
}

for i in range(2):
    for j in range(2, 4):
        if arr[i] == 