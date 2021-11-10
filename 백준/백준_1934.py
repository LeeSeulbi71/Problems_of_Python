# 최소공배수

Test_Num = int(input())

for i in range(Test_Num):
    A, B = map(int,input().split())

    for i in range(min(A,B), A*B+1):
        if i%A == 0 and i%B == 0:
            print(i)
            break
# 이렇게 풀면 시간초과!
# -> 유클리드 호제법으로 풀어야 함!

T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    print(lcm(A, B))
    
def gcd(a, b):
    return gcd(b%a, a) if b%a else a

def lcm(a, b):
    d = gcd(a, b)
    return d * (a//d) * (b //d)