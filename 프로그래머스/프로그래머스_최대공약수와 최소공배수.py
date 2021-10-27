#최대공약수: a,b를 나눌 수 있는 수 중 가장 큰 것
#최소공배수: a,b로 나눌 수 있는 수 중 가장 작은 것

def solution(n,m):
    answer = []
    for i in range(min(m,n), 0, -1):
        if m%i == 0 and n%i == 0:
            answer.append(i)
            break
    for j in range(max(m,n), m*n+1):
        if j%m == 0 and j%n ==0:
            answer.append(j)
            break
    return answer

print(solution(2,5))

#유클리드 호제법
# x, y의 최대공약수는 y,r의 최대공약수와 같다는 원리 이용 (x%y =r)

#최대공약수
def GCD(x,y):
    while(y): #y가 자연수일 때
        x, y = y, x%y
    return x
