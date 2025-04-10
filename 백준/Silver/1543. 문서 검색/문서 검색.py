import sys
input = sys.stdin.readline

arr = str(input().rstrip())
word = str(input().rstrip())
N = len(word)

def search(temp):    
    temp = temp.replace(word, '!')
    return temp.count('!')

answer = 0
temp = arr.replace(word, '!')
# for i in range(len(arr)-N):
#     copy = arr[i:]
#     answer = max(answer, search(copy))
print(temp.count('!'))
