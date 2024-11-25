import sys 
input = sys.stdin.readline

N, K = map(int, input().split())
score = []

for _ in range(N):
    score.append(float(input().rstrip()))

score.sort()

jScore = 0

for i in range(K,N-K): jScore+=score[i]
print('%.2f'%((jScore/(N-(2*K)) + 0.00000001)))

jScore += ((score[K]*K) + (score[N-K-1]*K))
print('%.2f'%((jScore/N) + 0.00000001))