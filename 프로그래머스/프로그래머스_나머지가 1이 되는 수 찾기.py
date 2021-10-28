def solution(n):
    answer = []
    for i in range(1, n):
        if n%i == 1:
            answer.append(i)
    return min(answer)

print(solution(12))

# 애초에 1부터 (작은 수부터) 하나씩 올라가니까
# 바로 i를 return 해줘도 됨!

def solution2(n):
    for i in range(1, n):
        if n%i == 1:
            return i

# if문이랑 for문 한 줄로 쓰는 거 연습하기