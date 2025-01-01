import sys
input = sys.stdin.readline

# 소수 배열을 다 구하고 누적합으로? 

N = int(input().rstrip())

if N == 1:
    print(0)
else:
    prime = []
    def is_prime_num(n):
        arr = [True]*(n+1)
        arr[0] = False
        arr[1] = False

        for i in range(2, n+1):
            if arr[i] == True:
                j = 2

                while (i*j) <= n:
                    arr[i*j] = False
                    j += 1 
        
        return arr

    arr = is_prime_num(N)

    for i in range(len(arr)):
        if arr[i]:
            prime.append(i)

    left, right, answer, sum = 0, 0, 0, prime[0]

    while left < len(prime)-1:
        if sum < N:
            right += 1
            sum += prime[right]
        elif sum == N:
            answer += 1
            right += 1
            sum += prime[right]
        else:
            sum -= prime[left]
            left+=1

    if sum == N:
        answer += 1

    print(answer)