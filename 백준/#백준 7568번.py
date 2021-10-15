n = int(input())

info = []
grade = []

for i in range(n):
    a, b = map(int, input(). split())
    info.append((a,b))

for i in range(n):
    count = 0
    for j in range(n):
        if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
            count +=1
    grade.append(count +1)

for d in grade:
    print(d, end=" ")