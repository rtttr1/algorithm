import sys

while True : 
    x, y, z = map(int, sys.stdin.readline().strip().split(' '))

    if x == 0 and y == 0 and z ==0 :
        break
    else :
        list = [x,y,z]
        list.sort()
        if pow(list[0], 2) + pow(list[1], 2) == pow(list[2],2) :
            print('right')
        else :
            print('wrong')