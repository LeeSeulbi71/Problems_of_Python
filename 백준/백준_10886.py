# 0=not cute 1=cute

The_Num_of_People = int(input())
survey_list = []

for person in range(The_Num_of_People):
    survey_list.append(input())

if survey_list.count('0') > survey_list.count('1'):
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")