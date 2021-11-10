# 약수들의 합

# 약수 입력 -> 약수들의 합으로 나타냄
# 완전수 아님 -> n is NOT perfect.

Num = int(input())
measure_list = []

for i in range(1, Num):
    if Num % i == 0:
        measure_list.append(i)

answer = f"{Num} = 1"
if sum(measure_list) == Num:
    for i in range(1, len(measure_list)):
        answer += f" + {measure_list[i]}"
    print(answer)
else:
    print(f"{Num} is NOT perfect.")