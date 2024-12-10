import sys
input = sys.stdin.readline

x = int(input().rstrip())

if x % 3 == 0:
    print('S')
elif x % 3 == 1:
    print('U')
else: 
    print('O')

