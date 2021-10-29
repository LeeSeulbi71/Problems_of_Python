# 연속적으로 나타나는 숫자 제거
# [1,3,0,1]

def solution(arr):
    answer = []
    answer.append(arr[0])
    print(answer)
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer

# 중복 풀 때는 i+1 보다는 i-1을 쓰자
# 처음 거는 새 리스트에 추가해두고 그 다음부터 비교해서 추가할 수 있도록
print(solution([1,1,3,3,0,1,1]))