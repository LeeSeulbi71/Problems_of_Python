def solution (array, commands):
    answer_num = []
    for n in range(len(commands)):
        i = commands[n][0]
        j = commands[n][1]
        k = commands[n][2]
        selected_array = array[i-1:j]
        selected_array.sort()
        answer_num.append(selected_array[k-1])
    return answer_num

print(solution([1,5,2,6,3,7,4], [[2,5,3], [4,4,1], [1,7,3]]))