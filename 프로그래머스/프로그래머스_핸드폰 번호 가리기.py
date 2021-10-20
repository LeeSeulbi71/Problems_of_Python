def solution(phone_number):
    phone_number_to_list = list(phone_number[:-4])
    list_to_str = ''
    for i in range(len(phone_number_to_list)):
        phone_number_to_list[i] = '*'
    for j in phone_number_to_list:
        list_to_str += j

    answer = list_to_str + phone_number[-4:]
    return answer

print(solution("01033334444"))

# 문자열 곱셈 가능
# 문자열 리스트로 바꿀 필요 없음 - len 쓸 때

def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]