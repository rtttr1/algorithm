import sys

input = sys.stdin.readline

um = list(map(str, input().split()))
um = ''.join(um)

if um == '12345678':
    print('ascending')
elif um == '87654321':
    print('descending')
else:
    print('mixed')