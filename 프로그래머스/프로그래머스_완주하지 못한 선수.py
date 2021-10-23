def solution(participant, completion):
    new_participant = []
    for i in participant:
        if i not in new_participant:
            new_participant.append(i)
        else:
            new_participant.remove(i)

    if new_participant == participant:
        for i in participant:
            if i in completion:
                continue
            elif i not in completion:
                return i
    else:
        for j in completion:
            if j in new_participant:
                continue
            elif j not in new_participant:
                return j

print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))

#participant[i]해서 competition에 있는지 확인 후 있으면 삭제
#없으면 반환

def solution2(participant, completion):
    answer = ''
    for i in range(len(participant)):
        if participant[i] in completion:
            completion.remove(participant[i])
        else:
            answer = participant[i]
            break
    return answer
print(solution2(["leo", "kiki", "eden"], ["eden","kiki"]))

#차집합 교집합 합집합

def solution3(participant, completion):
    participant.union
