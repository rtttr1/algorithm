import random

# 1부터 100 사이의 난수 발생
randomNum = random.randint(1, 100)
print("컴퓨터 생성 숫자: ", randomNum)



for i in range(100):
    answer = int(input("1~100사이의 숫자를 맞춰보세요: "))
    if answer < randomNum :
        print('입력한 숫자가 작습니다.')
    elif answer > randomNum :
        print("입력한 숫자가 큽니다.")
    else :
        print("축하합니다. 시도횟수는 %d번 입니다." % (i+1))
        break