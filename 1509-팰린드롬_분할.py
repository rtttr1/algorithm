import sys
input = sys.stdin.readline

N,M = map(int,input().split())
print(abs(N-M))
arr = str(input().rstrip())
N = len(arr)

pelins = []
dp = [0]*N

def isPelin():
    
    
