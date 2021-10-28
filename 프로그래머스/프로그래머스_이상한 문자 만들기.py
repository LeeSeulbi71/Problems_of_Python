# split -> 2차원 리스트
# for i in range(len(first_list))
# for j in range(len(second_list[i])) -> 중첩반복문
# if 짝수 .upper(j)
# else .lower(j)

def solution(s):
    string_list = list(map(list,s.split()))
    for i in range(len(string_list)):
        for j in range(len(string_list[i])):
            if j % 2 == 0:
                string_list[i][j] = string_list[i][j].upper()
            else:
                string_list[i][j] = string_list[i][j].lower()
    for k in range(len(string_list)):
        string_list[k] = "".join(string_list[k])
    string_list = " ".join(string_list)
    return string_list
print(solution("try hello world"))