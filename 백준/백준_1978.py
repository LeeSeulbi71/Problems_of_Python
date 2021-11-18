#소수 찾기

count = int(input())
num = list(int(input().split()))
decimal = 0

for i in num:
    error = 0
    if i  > 1:
        for j in range(2, i):
            if i % j == 0:
                error += 1
        if error == 0:
            decimal += 1

print(decimal)