#while != 1
#if 짝수 2로 나눔
#else 3으로 나눔 + 1
#count

def solution(num):
    answer = 0
    while (num != 1):
        if (num%2 == 0):
            num = num/2
            answer += 1
        else:
            num = num *3 +1
            answer += 1
    if answer >=500:
        answer = -1
    return answer

print(solution(626331))