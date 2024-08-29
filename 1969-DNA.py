import sys 

N, M = map(int, sys.stdin.readline().strip().split(' '))

DNAs = []
elem = ['A', 'C', 'G', 'T']

for _ in range(N) :
    DNAs.append(sys.stdin.readline().strip())

answer = ''
hd = 0

for i in range(M) :
    count = [0, 0, 0, 0]
    for j in range(N) :
        if DNAs[j][i] == 'A' : count[0] += 1
        elif DNAs[j][i] == 'C' : count[1] += 1
        elif DNAs[j][i] == 'G' : count[2] += 1
        elif DNAs[j][i] == 'T' : count[3] += 1
    answer += elem[count.index(max(count))]
    for i in count :
        hd += i
    hd -= max(count) 

print(answer)
print(hd)