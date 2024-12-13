import sys
input = sys.stdin.readline

one, two, three, people = map(int, input().split())

if people % one == 0 or people % two == 0 or people % three == 0:
    print(1)

    