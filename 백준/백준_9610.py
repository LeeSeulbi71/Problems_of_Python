#사분면

Test_num = int(input())

Quantile = [0, 0, 0, 0]
Axis = 0

for i in range(Test_num):
    A, B = map(int, input().split())
    
    if A>0 and B>0:
        Quantile[0] += 1
    elif (A<0 and B>0):
        Quantile[1] += 1
    elif (A<0 and B<0):
        Quantile[2] += 1
    elif (A>0 and B<0):
        Quantile[3] += 1
    else: 
        Axis += 1

    print(A, B, Quantile, Axis)

for i in range(4):
    print(f'Q{i+1}: {Quantile[i]}')
print(f'AXIS: {Axis}')
