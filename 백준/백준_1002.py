#터렛

#slipt -> list
#list_jo랑 list_baek으로 나누기

import math

T_num = int(input())

for T in range(T_num):
    list_all = list(map(int, input().split()))
    list_jo = list_all[0:3]
    list_baek = list_all[3:]

    distance_between_center = math.sqrt(pow(list_jo[0]-list_baek[0], 2)+pow(list_jo[1]-list_baek[1], 2))
    sum_of_radius = list_jo[2] + list_baek[2]

    if distance_between_center == 0 and list_jo[2] == list_baek[2]:
        print(-1)
    elif abs(list_jo[2]-list_baek[2]) == distance_between_center or distance_between_center == sum_of_radius:
        print(1)
    elif abs(list_jo[2]-list_baek[2]) < distance_between_center < sum_of_radius:
        print(2)
    else:
        print(0)