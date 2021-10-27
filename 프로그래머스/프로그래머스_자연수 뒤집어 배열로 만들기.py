def solution(n):
    answer_new = []
    n = list(str(n))
    answer = (n[::-1])
    for i in answer:
        answer_new.append(int(i))
    return answer_new

print(solution(12345))

#다른 사람 풀이

def digit_reverse(n):
    return list(map(int, reversed(str(n))))

#int를 써야할 땐 map을 떠올리자....!