#나눠서 리스트
#for int로 바꿔서 더하기

def solution(n):
    answer = 0
    n = list(str(n))
    for i in n:
        answer += int(i)
    return answer

print(solution(987))