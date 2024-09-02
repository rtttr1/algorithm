import sys

T = int(sys.stdin.readline().strip())
answer = []
for _ in range(T) :
    A, B = map(int, sys.stdin.readline().strip().split(' '))
    Aarr = []
    Barr = []

    while A != 0 :
        Aarr.append(A)
        A = A // 2 
        
    while B != 0 :
        Barr.append(B)
        B = B // 2
        

    for elem in Aarr :
        if elem in Barr :
            answer.append(elem*10)
            break

for elem in answer :
    print(elem)