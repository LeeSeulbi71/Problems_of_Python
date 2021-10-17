# 숫자 찾기 게임

import random

guess_number = random.randint(1,100) #1~100 사이 정수 난수 발생

print("숫자를 맞추보세요. (1~100)")

user_input = int(input())

while(user_input is not guess_number): #입력값이 틀리는 동안 계속 실행
    if user_input > guess_number:
        print("숫자가 너무 큽니다.")
    else:
        print("숫자가 너무 작습니다.")
    user_input = int(input())

print("정답입니다. 입력한 숫자는 ", user_input, "입니다.")