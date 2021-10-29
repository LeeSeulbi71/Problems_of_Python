# 아스키 코드 이용

def solution(s,n):
    s = list(s)
    new_s = []
    for i in s:
        if ord(i) == 32:
            new_s.append(" ")
        else:
            if (ord(i) + n) > 91:
                (ord(i) + n) 
            new_s.append(chr(ord(i) + n))
    return "".join(new_s)

print(solution("z", 1))