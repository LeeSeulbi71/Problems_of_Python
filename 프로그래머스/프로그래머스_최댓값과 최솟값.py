def solution(s):
    answer_list = []
    s_list = list(map(int, s.split()))
    answer_list.append(min(s_list))
    answer_list.append(max(s_list))
    answer_to_str = [str(i) for i in answer_list]
    answer = " ".join(answer_to_str)
    return answer
print(solution('-1 -1'))

# 다른 사람 풀이

def solution(s):
    s = list(map(int, s.split()))
    return str(min(s)) + " " + str(max(s))