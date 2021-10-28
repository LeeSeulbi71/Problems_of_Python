#리스트에 약수 구하기
#sum (리스트)

def solution(n):
    answer = []
    for i in range(n, 0, -1):
        if n%i == 0:
            answer.append(i)
    return sum(answer)

print(solution(5))