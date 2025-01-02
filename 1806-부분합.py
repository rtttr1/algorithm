import sys
input = sys.stdin.readline

N, S = map(int, input().split())

if S == 0:
    print(1)
else:
    arr = list(map(int, input().split()))

    left, right, sum, answer = 0, 0, arr[0], 10e9

    while left < N:
        if sum >= S:
            answer = min(answer, right - left + 1)
            sum -= arr[left]
            left += 1
            
        elif sum < S:
            if right+1 < N:
                right += 1
                sum += arr[right]
            elif right == N-1 and left + 1 < N:
                sum -= arr[left]
                left += 1
            else:
                break
        
    if answer == 10e9 or answer <= 0:
        print(0)
    else:
        print(answer)