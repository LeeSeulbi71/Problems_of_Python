# 약수 구하는 거랑 비슷하게 접근
# for i in range(1, n+1):
# 중첩반복문 for j in range(i, 0, -1):
# 만약 약수의 개수 = 3이상 X
# count += 1

def solution(n):
    answer = 0
    for j in range(2, n+1):
        if prime(j) == 1:
            answer += 1
    return answer

def prime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return 0
    return 1

print(solution(100))

# 알고리즘 - 에라토스테네스의 체
# 다른 사람 풀이

def solution(n):
    num = set(range(2, n+1))

    for i in range(2, n+1):
        if i in num:
            num -= set(range(2*1, n+1, i))
    return len(num)