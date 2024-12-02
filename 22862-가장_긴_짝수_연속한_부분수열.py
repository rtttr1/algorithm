import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = list(map(int, input().split()))

left, right, d, temp, answer  = 0, 0, 0, 0, 0

if S[0] % 2 == 1: d += 1
else: 
    temp += 1
    answer += 1

while right < N-1:
    if d <= K:
        right += 1
        if S[right] % 2 == 1:
            d += 1
        else:
            temp += 1
    else:
        if S[left] % 2 == 1:
            d-= 1
        else: 
            temp -= 1
        left += 1
    answer = max(answer, temp)

print(answer)
            

