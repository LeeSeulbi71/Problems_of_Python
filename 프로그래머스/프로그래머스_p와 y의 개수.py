def solution(s):
    s = s.lower()
    if s.count('p') == s.count('y'):
        return True
    else:
        return False

print(solution("pYY"))

# 다른 사람 풀이
# 메소드 연결해서 쓸 수 있다는 거 잊지 말기

def solution2(s):
    return s.lower().count('p') == s.lower().count('y')