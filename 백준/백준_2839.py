#설탕 배달

N = int(input())
count = 0



while N//5 != 0:
    count += N//5
    N = N%5
    if ((N%5 or N%3) in [1,2,4]):
        print(-1)
if N == 0:
    print(count)
while N//3 != 0:
    count += N//3
    N = N%3
    if ((N%5 or N%3) in [1,2,4]):
        print(-1)
    if N == 0:
        print(count)
    

    

