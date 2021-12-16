#분해합

num = int(input())

storage = []

for i in range(1, num):
    split_list = list(str(i))
    if i+sum([int(j) for j in split_list]) == num:
        storage.append(i)

print(min(storage))