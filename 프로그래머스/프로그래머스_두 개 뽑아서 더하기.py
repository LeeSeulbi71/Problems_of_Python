# 월코 시즌 1
# 중첩 반복문 - 리스트 추가
# set으로 중복 제거
# sorted로 오름차순

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                answer.append(numbers[i] + numbers[j])
            else: continue
    answer = sorted(set(answer))
    #sorted는 어떤 iterable 객체라도 받을 수 있음

    return answer

print(solution([5,0,2,7]))

#나랑 되게 비슷하긴 한데 다른 풀이

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)): #if 안쓰려고 i+1
            answer.append(numbers[i]+numbers[j])
    
    return sorted(list(set(answer))) #바로 return 값에 set & sorted