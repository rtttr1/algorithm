import sys
input = sys.stdin.readline

N, K = map(int, input().split())
meetings = []

for _ in range(N): 
    meetings.append(list(map(int, input().split())))

meetings.sort(key= lambda x:(x[1], -x[0]))
times = [0]*K
answer = 0

for start, end in meetings:
    times.sort(reverse=True)
    for i in range(K):
        if times[i] < start :
            times[i] = end
            answer += 1
            break

print(answer)