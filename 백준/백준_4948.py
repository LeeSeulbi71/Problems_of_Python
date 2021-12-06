#베르트랑 공준 -- 이 코드 고치기 !!!

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

def sosu(n):
    if n ==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True							#소수 구하는 방식은 위와 같다

all_list = list(range(2,246912))		#문제에서 제한한 범위
memo = []								#for문 밖에 리스트 정의

for i in all_list:						#2부터 2*123,456 범위
    if sosu(i):							#sosu함수에 해당하면
        memo.append(i)					#리스트에 추가

n = int(input())

while True:
    count=0					#갯수를 세야하는 조건 때문에 카운트
    if n == 0 :
            break
    for i in memo:			#memo리스트 중에서
        if n < i <=2*n:		#입력한 값의 범위 내에서 값이 있으면
            count+=1		#있을 때 마다 카운트 +1
    print(count)
    n = int(input())		#0 입력받기 전까지 계속 해야하므로 입력 받음