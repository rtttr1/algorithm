import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

graph = [list(map(int, input().rstrip())) for _ in range(N)]

