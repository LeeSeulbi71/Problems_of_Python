#각 자리수 나눠서 더하기
#나눠서 0인지 확인

def solution(x):
    number = list(str(x))
    new_x = 0
    for i in number:
        new_x += int(i)
    if ((x % new_x) == 0):
        return True
    else:
        return False

print(solution(13))

#다른 사람 풀이

def Harshad(n):
    return n % sum([int(c) for c in str(n)]) == 0