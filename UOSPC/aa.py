import sys
input = sys.stdin.readline

S = int(input().rstrip())
F = int(input().rstrip())

if S > F: print('flight')
else: print('high speed rail')