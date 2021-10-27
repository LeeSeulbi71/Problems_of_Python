def solution(arr1, arr2):
    answer = []#각각 만들어서 리스트 자체를 추가하기
    semi = []
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            semi.append(arr1[i][j] + arr2[i][j])
        answer.append(semi)
        semi = []
    return answer

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))

#다른 사람 풀이

def sumMatrix(A,B):
    answer = [[c+d for c,d in zip(a,b)] for a, b in zip(A,B)]
    return answer

#이건 사람의 수준을 벗어난 것 같다...........
#같이 돌아야 할 때는 이제 ij에서 벗어나 zip으로......

print(sumMatrix([[1], [2]], [[3], [4]]))