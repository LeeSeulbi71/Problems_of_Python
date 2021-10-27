#sorted 함수
#list로 받기

def solution(n):
    new_n = list(str(n))
    #sorted는 어짜피 리스트로 반환
    new_n = sorted(new_n, reverse=True)
    answer = int("".join(new_n))
    #list to string -> 빈문자열.join(리스트)
    return answer

print(solution(118372))