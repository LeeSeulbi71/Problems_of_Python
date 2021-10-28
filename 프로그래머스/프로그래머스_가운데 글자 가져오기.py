def solution(s):
    if len(s)%2 == 0:
        a = int(len(s)/2-1)
        return s[a:a+2]
    else:
        return s[int((len(s)-1)/2)]

print(solution("qwer"))
