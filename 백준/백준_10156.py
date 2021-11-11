# 과자

# 과자값 * 개수 > 현재 돈 -> 차액 계산
# 아니면 0

def from_parents(price_of_snack, snack, dongsu_money):
    need_money = price_of_snack * snack

    if need_money > dongsu_money:
        return need_money - dongsu_money
    else:
        return 0

price_of_snack, snack, dongsu_money = map(int, input().split())
print(from_parents(price_of_snack, snack, dongsu_money))
