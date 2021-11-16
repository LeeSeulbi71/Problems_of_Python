#수들의 합

Sum_Num = int(input())
n = 1
make_Sum = 1
count = 0

while make_Sum != Sum_Num:
    n += 1
    make_Sum += n
    count +=1

print(count)