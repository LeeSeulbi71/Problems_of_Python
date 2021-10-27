#약수 개수 구해서 append
#짝수면 더하고 홀수면 빼기

def solution(left, right):
    answer_list = []
    count = 0
    answer = 0
    number_list = list(range(left, right+1))

    for i in range(left, right+1):
        for j in range(i, 0, -1):
            if i%j == 0:
                count += 1
        answer_list.append(count)
        count = 0

    for k, n in zip(answer_list, number_list):
        if k%2 == 0:
            answer += n
        else:
            answer -= n

    return answer

print(solution(24, 27))

# 다른 사람 풀이
# 제곱수는 약수의 개수가 홀수..............

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if int(i**0.5) == i**0.5:
            answer -= i
        else:
            answer += i
    return answer