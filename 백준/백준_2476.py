# 주사위 게임

n = int(input())

max_reward = 0

for _ in range(n):
    reward = 0 
    d1, d2, d3 = map(int, input().split())
    if d1 == d2 == d3:
        reward = 10000 + d1 * 1000
    elif d1 == d2:
        reward = 1000 + d1 * 100
    elif d2 == d3:
        reward = 1000 + d2 * 100
    elif d1 == d3:
        reward = 1000 + d1 * 100
    elif d1 != d2 != d3:
        reward = max(d1, d2, d3) * 100
    if max_reward < reward:
        max_reward = reward

print(max_reward)