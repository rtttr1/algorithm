import sys
input = sys.stdin.readline

arr = list(map(str,input().rstrip()))
answer = ''
for elem in arr:
    if elem.isupper():
        answer += elem.lower()
    else:
        answer += elem.upper()
print(answer)