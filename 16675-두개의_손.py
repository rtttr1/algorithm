import sys
input = sys.stdin.readline

arr = list(map(str, input().split()))

RSP = {
    'R': 'P',
    'P': 'S',
    'S': 'R'
}

if arr[0] == arr[1]:
    if RSP[arr[0]] in arr[2:4]:
        print('TK')
    elif RSP[arr[2]] == arr[0] or RSP[arr[3]] == arr[0]:
        print('MS')
    else:
        print('?')
    
elif arr[2] == arr[3]:
    if RSP[arr[2]] in arr[0:2]:
        print('MS')
    elif RSP[arr[0]] == arr[2] or RSP[arr[1]] == arr[2]:
        print('TK')
    else:
        print('?')
else:
    print('?')

