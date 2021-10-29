# ["sun", "bed", "car"]	1	["car", "bed", "sun"]
# strings[i][n]

def solution(strings, n):
    semi_answer = []
    for i in range(len(strings)):
        semi_answer.append(strings[i][n])
    #for k, n in zip(semi_answer, strings):

print(solution(['sun', 'bed', 'car'], 1))