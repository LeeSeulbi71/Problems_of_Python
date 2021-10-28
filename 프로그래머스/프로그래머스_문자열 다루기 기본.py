def solution(s):
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        return True
    else:
        return False

print(solution("1234"))

# 다른 사람 풀이

def alpha_string46(string):
    return s.isdigit() and len(s) in (4,6)