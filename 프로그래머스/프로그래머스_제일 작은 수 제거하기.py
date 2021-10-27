#리스트 받고
#min 함수 쓰기
#만약 min = 원래 -> -1 리턴

def solution(arr):
    if [min(arr)] == arr:
        return [-1]
    else:
        arr.remove(min(arr))
        return arr
        
print(solution([1,2,3,4]))