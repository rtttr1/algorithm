import sys
input = sys.stdin.readline

arr1 = str(input().rstrip())
arr2 = str(input().rstrip())

if len(arr1) >= len(arr2):
    print('go')
else:
    print('no')