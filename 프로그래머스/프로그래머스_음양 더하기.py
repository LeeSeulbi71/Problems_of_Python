def solution(ablsoutes, signs):
    answer = 0
    for i in range(len(signs)):
        if str(signs[i]) == 'False':
            answer -= ablsoutes[i]
        else:
            answer += ablsoutes[i]
    return answer

#if-else로 한 줄로 작성
def solution(absolutes, sign):
    return sum(absolutes if sign else -absolutes, sign in zip(absolutes, signs))