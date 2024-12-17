import sys
input = sys.stdin.readline

one, two, three, people = map(int, input().split())

answer = 0
for i in range(50):
    for j in range(50):
        for k in range(50):
            if one*i + two*j + three*k == people:
                answer = 1
                break
       
print(answer)