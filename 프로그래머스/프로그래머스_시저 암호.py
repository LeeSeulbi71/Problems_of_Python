# 아스키 코드 이용

def solution(s,n):
    s = list(s)
    new_s = []
    for i in s:
        to_number = ord(i)
        if to_number == 32:
            new_s.append(" ")
        elif 91<= (to_number+n) <=96:
            to_number = 64 + n
            new_s.append(chr(to_number))
        elif (to_number+n) >= 123:
            to_number = 96+n
            new_s.append(chr(to_number))
        else:
            new_s.append(chr(to_number+n))
    return "".join(new_s)

print(solution("a B z", 4))