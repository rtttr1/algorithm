import sys 
input = sys.stdin.readline

T = int(input().rstrip())

for i in range(T):
    N = int(input().rstrip())
    arr = list(map(int, input().split()))

    while len(arr) > 2:
        temp = []
        for j in range(len(arr) // 2):
                temp.append(arr[j] + arr[len(arr) - j - 1])
        if len(arr) % 2 == 1:
             temp.append(arr[len(arr) // 2] * 2)
        arr = temp
    
    if arr[0] > arr[1]: print("Case #{}: Alice".format(i+1))
    else : print("Case #{}: Bob".format(i+1))
           
