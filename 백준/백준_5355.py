#화성 수학

#인수를 여러 개 받는 함수 -> arg
#계산하는 함수

Test_num = int(input())

def calculator(Num, string):
        if string == '@':
            return Num *3
        elif string == '%':
            return Num +5
        else:
            return Num -7

for i in range(Test_num):
    lists = list(map(str, input().split()))
    
    print(lists)
    Num = float(lists[0])
    Next_Num = calculator(Num, lists[1])
    print(Next_Num)

    for j in range(2, len(lists)):
        Next_Num = calculator(Next_Num, lists[j])
        print(Next_Num)
    print("{:.2f}".format(Next_Num))