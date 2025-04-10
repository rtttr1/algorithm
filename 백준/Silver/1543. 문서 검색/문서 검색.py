import sys
input = sys.stdin.readline

arr = str(input().rstrip())
word = str(input().rstrip())
N = len(word)

temp = arr.replace(word, '!')
print(temp.count('!'))
