#Split에 따라 나누기
#만약 첫 글자가 영문이면 upper()
#아니면 나머지 전부 다 lower()
#" ".join(리스트)

def solution(s):
    JadenCase = list(s.split())

    for i in range(len(JadenCase)):
        if JadenCase[i][0].isalpha():
            JadenCase[i] = JadenCase[i][0].upper() + JadenCase[i][1:].lower()
        else:
            JadenCase[i] = JadenCase[i][0] + JadenCase[i][1:].lower()
    
    return " ".join(JadenCase)

print(solution("for the last week"))

def solution(s):
    s = s.lower()
    L=s.split(" ")
    answer = ""
    for i in L:
        i= i.capitalize()
        answer+= i+" "
    return answer[:-1]