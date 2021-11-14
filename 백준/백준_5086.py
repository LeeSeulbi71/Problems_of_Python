# 배수와 약수

while 1:

    A, B = map(int, input().split())

    if (A==0 & B==0):
        break
    elif A%B == 0:
        print('multiple')
    elif B%A == 0:
        print('factor')
    else:
        print('neither')