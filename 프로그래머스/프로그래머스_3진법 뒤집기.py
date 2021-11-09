def solution(n):
    answer = 0
    while ((n//3) not in [0,1,2]): 
        list_10_3.append(n%3)
        n = n//3
    list_10_3.extend([n%3, n//3])

    for i in range(len(list_10_3)):
        answer += list_10_3[i]*(pow(3, len(list_10_3)-1-i))
    
    return answer

print(solution(1))