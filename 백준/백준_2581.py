#소수

M = int(input())
N = int(input())

decimal = []

for i in range(M, N+1):
    error = 0
    if i  > 1:
        for j in range(2, i):
            if i % j == 0:
                error += 1
                break
        if error == 0:
            decimal.append(i)

if len(decimal) > 0:
    print(sum(decimal))
    print(min(decimal))
else:
    print(-1)