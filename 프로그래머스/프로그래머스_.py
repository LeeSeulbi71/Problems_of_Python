#어떤 단어가 여기 있나?로 확인
from abc import abstractproperty


def solution(s):
    answer = []
    number = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

    for j in s:
        if j.isdigit() != True:
            for i in number:
                if i in s: 
                    i = number.get(i)
                    answer.append(i)
                    print(i)
                    print(answer)
        else:
            answer.append(j)
            print(answer)
        return answer

print(solution("one4seveneight"))