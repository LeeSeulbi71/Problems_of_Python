# 연속적으로 나타나는 숫자 제거
# [1,3,0,1]

def solution(arr):
    new_arr = []
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            new_arr.append(arr[i])
    return new_arr

print(solution([4,4,4,3,3]))