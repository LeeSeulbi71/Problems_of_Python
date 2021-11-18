#소수

M = int(input())
N = int(input())

num = list(range(M, N+1))
decimal = []

for i in num:
    error = 0
    for j in range(2, i):
        if i % j == 0:
            error += 1
    if error == 0:
        decimal.append(i)

if len(decimal) > 0:
    print(sum(decimal))
    print(min(decimal))
else:
    print(-1)