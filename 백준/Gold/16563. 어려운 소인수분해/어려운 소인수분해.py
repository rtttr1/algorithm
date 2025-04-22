import sys
import math
input = sys.stdin.readline

N = int(input().rstrip())
K = list(map(int, input().split()))

MAX = max(K)
isPrime = [True] * MAX
primeArr = []

for i in range(2, int(math.sqrt(MAX)) + 1):
    if isPrime[i] == True:
        primeArr.append(i)
    for j in range(i*i, MAX, i):
        isPrime[j] = False

for num in K: 
    for prime in primeArr: 
        if prime > num: break

        if num % prime == 0:
            while num % prime == 0: 
                num = num // prime
                print(prime, end=' ')
    if num > 1:
        print(num)
    else:
        print()
