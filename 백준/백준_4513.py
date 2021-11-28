#직각삼각형

while 1:
    num = list(map(int, input().split()))
    max_num = max(num)
    num.remove(max_num)

    if sum(num) == 0:
        break
    elif pow(max_num, 2) == (pow(num[0], 2)+pow(num[1],2)):
        print('right')
    else:
        print('wrong')
