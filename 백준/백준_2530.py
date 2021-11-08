#인공지능 시계

present_time = list(map(int, input().split()))
taken_time = int(input())

take_time_list = []
take_time_list.append(taken_time % 60)
take_time_list.append(taken_time // 60 % 60)
take_time_list.append(taken_time // 60 // 60)
print(take_time_list)

take_time_list.reverse()
print(present_time, take_time_list)

done_time = [0, 0, 0]
for i in range(3):
    done_time[i] = take_time_list[i] + present_time[i]

if done_time[2] >= 60:
    done_time[2] -= 60
    done_time[1] += 1
if done_time[1] >= 60:
    done_time[1] -= 60
    done_time[0] += 1
if done_time[0] >= 24:
    done_time[0] -= 24

answer = []
for i in done_time:
    answer.append(str(i))
answer_to_str = " ".join(answer)
answer_to_int = map(int, answer_to_str.split())
print(answer_to_int)
