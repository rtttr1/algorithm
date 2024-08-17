import sys

M, N = map(int, sys.stdin.readline().split())

sieve = [False, False] + [True] * (N - 1)
primes = []

for i in range(2, N + 1):
    if sieve[i]:
        if i >= M:
            primes.append(i)
        for j in range(2 * i, N + 1, i):
            sieve[j] = False

for el in primes:
    print(el)
