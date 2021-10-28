def solution(arr, divisor):
    answer = []
    for i in arr:
        if i%divisor == 0:
            answer.append(i)
    if answer == []:
        answer.append(-1)
    return sorted(answer)

print(solution([2,36,1,3], 1))

# 다른 사람 풀이

def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]

# 파이썬은 or 앞이 참일 경우 앞의 값까지만, 거짓일 경우 뒤에 것 호출