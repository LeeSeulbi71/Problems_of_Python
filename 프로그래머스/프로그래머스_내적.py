def solution(a, b):
    scalar_product = 0
    for i in range(len(a)):
        scalar_product += a[i] * b[i]
    answer = scalar_product
    return answer

print(solution([-1,0,1], [1,0,-1]))

#zip 함수 사용

def solution(a,b):
    return sum([x*y for x,y in zip(a,b)])

#a와 b리스트의 튜플을 돌면서 각각의 값 호출
#여러 그룹의 데이터를 루프를 한 번만 돌면서 처리