import sys
input = sys.stdin.readline

A = int(input().rstrip())
arr = list(map(int, input().split()))

def Binary_search(target):
    low = 0
    high = A-1

    while low < high:
        mid = (low + high) // 2

        if mid == target:
            