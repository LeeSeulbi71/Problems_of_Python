#오븐 시계

hour, minute = map(int, input().split())
taked_time = int(input())

answer_minute = minute + taked_time
answer_hour = hour

while ((answer_minute>=60) or (answer_hour>23)):
    if answer_minute >=60:
        answer_hour += 1
        answer_minute -= 60

    elif answer_hour >23:
        answer_hour = 0

print(answer_hour, answer_minute)