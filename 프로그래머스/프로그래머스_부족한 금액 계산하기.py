# price -> for 문 돌려서 필요한 돈의 수 계산
# 필요한 돈에서 money 빼기

def solution(price, money, count):
    need_money = 0
    for i in range(1, count+1):
        need_money += price * i
    if need_money - money < 0:
        return 0
    else:
        return need_money - money
print(solution(3,20,4))

# 다른 사람 풀이

def solution(price, money, count):
    return max(0, price*(count+1)*count//2-money)

# 등차수열의 합 공식