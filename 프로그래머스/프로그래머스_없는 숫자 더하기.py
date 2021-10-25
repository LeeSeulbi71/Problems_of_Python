#answer = 0
#for 문으로 하나씩 검사해서 answer에 더하기
#월코 시즌2

def solution(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers:
            answer += i
    return answer