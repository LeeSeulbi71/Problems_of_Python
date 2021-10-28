def solution(s):
    s = sorted(s, reverse = True)
    return "".join(s)

# s에 안 넣고 바로 join에 넣을 수 있음

print(solution("Zbcdefg"))