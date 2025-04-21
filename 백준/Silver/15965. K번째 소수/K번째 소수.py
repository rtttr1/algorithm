import sys
import math
input = sys.stdin.readline

K = int(input().rstrip())

MAX = 10000000
prime = [True for i in range(MAX+1)]
prime[1] = False

for i in range(2, int(math.sqrt(MAX))+1):
    if prime[i] == True:
        j = 2
        while i*j <= MAX:
            prime[i*j] = False
            j+=1

count = 0
for i in range(2, MAX+1):
    if prime[i]:
        count += 1
    if count == K:
        print(i)
        break