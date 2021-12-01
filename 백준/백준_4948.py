#베르트랑 공준

def isPrime(num):
    check = []
    if num==1:
        return 1
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                continue
            else:
                check.append(i)
        return len(check)
        


while 1:
    check = []
    N = int(input())
    for i in range(N, N+N+1):
        print(isPrime(i))
    if N == 0:
        break

# 에라토스테네스의 체로 풀어보기 !!

