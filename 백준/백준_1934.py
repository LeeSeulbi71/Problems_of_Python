# 최소공배수

Test_Num = int(input())

for i in Test_Num:
    A, B = map(int,input().split())

    for i in range(min(A,B), A*B+1):
        if i%A == 0 and i%B == 0:
            print(i)
            break
