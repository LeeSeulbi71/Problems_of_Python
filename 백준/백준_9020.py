#골드바흐의 추측

#2보다 큰 짝수는 소수로 표현됨
#일단 수를 입력받음
#소수로 짝수를 만든다.....
#모르겠넹 ....

def Goldbach():
    check = [False, False] + [True] * 10000 #입력값이 10000가지 주어질 수 있기 때문에 
    # 길이가 0, 1 (1,2) 인덱스가 Flase이고 나머지 True인 길이가 10002인 check라는 리스트를 만듦

#아레테네스의 체 - 소수 리스트!
    for i in range(2, 101):
        if check[i] == True:
            for j in range(i+i, 10001, i):
                check[j] = False
    
    T = int(input()) #테스트 개수
    for _ in range(T):
        n = int(input()) #숫자 입력 
        A = n//2 #절반부터 탐색 -> 8 = 4+4
        B = A
        for _ in range(10000):
            if check[A] and check[B]:
                print(A, B)
                break
            A-=1
            B+=1

Goldbach()