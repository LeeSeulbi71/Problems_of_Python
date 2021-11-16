#수들의 합

s = int(input())
total = 0
count = 0

while 1:
    count += 1
    total += count
    if total > s:
        break

print(count-1)