def solution(participation, completion):
    participation.sort()
    completion.sort()
    for p,c in zip(participation, completion):
        if p != c:
            return p
    return participation.pop()