### 주사위 세 개

dice = list(map(int, input().split()))
init_dice = dice
dice = list(set(dice))

if len(dice) == 0:
    print(10000+init_dice[0]*1000)
elif len(dice) == 2:
    sum_dice = init_dice + dice
    if sum_dice.count(dice[0]) < sum_dice.count(dice[1]):
        print(1000+init_dice[1]*100)
    else:
        print(1000+init_dice[0]*100)
else:
    print(max(dice)* 100)