### 주사위 게임

Participants = int(input())
Participants_list = []

for participant in range(Participants):
    dice = list(map(int, input().split()))
    init_dice = dice
    dice = list(set(dice))

    if len(dice) == 1:
        reward = (10000+init_dice[0]*1000)
    elif len(dice) == 2:
        sum_dice = init_dice + dice
        if sum_dice.count(dice[0]) < sum_dice.count(dice[1]):
            reward = 1000+init_dice[1]*100
        else:
            reward = 1000+init_dice[0]*100
    else:
        reward = max(dice)* 100
    
    Participants_list.append(reward)

print(Participants_list)

print(max(Participants_list))