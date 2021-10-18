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
    


