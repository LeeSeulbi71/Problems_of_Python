# 구구단 계산기

num = int(input("구구단 몇 단을 계산할까요? \n"))
print("구구단 {}단을 계산합니다.".format(num))

for i in range(1,10):
    print("{0} X {1} = {2}".format(num, i, num*i))