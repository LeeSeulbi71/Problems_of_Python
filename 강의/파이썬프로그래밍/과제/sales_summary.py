def sort_sales(data):
    #===== write your code below =======
    #튜플을 리스트로 ~!
    new_data = []
    for i in range(len(data)):
        new_data.append(list(data[i]))

    #최종 데이터에 넣을 값 중 더해야 하는 값만 일단 final_data에 추가
    final_data =[]
    for i in range(len(new_data)):
        for j in range(i+1, len(new_data)):
            if new_data[i][0] == new_data[j][0]:
                    final_data.append((new_data[i][0], new_data[i][1]+new_data[j][1]))

    #fianl_data에 없는 값들을 추가하기 위한 name_list(중복 확인용)
    final_name_list = []
    for i in range(len(final_data)):
        if final_data[i][0] not in final_name_list:
            final_name_list.append(new_data[i][0])
    
    #fianl_data 완성!
    for i in range(len(new_data)):
            if new_data[i][0] not in final_name_list:
                final_data.append((new_data[i][0], new_data[i][1]))
            
    #판매량 기준으로 내림차순
    sorted_data = sorted(final_data, key=lambda x: x[1], reverse=True)
    return sorted_data


def sales_summary(data):
    #===== write your code below =======
    # for 문으로 돌면서
    # 일단 제일 처음 1
    # 두 번째가 같으면 그 전이랑 같게
    # for i in range(len(data)):
    
    #내림차순으로 정리했으니 1번은 무조건 1위
    data[0] += (1,)

    for i in range(1, len(data)):
        if data[i-1][1] != data[i][1]:
            if len(data[i])>2:
                continue
            else:
                if data[i-1][1] == data[i-2][1]:
                    data[i] += (data[i-1][2]+2, )
                else:
                    data[i] += (data[i-1][2]+1, )
        else:
            if len(data[i])<=2:
                data[i] += (data[i-1][2], )


    
    return data

if __name__ == '__main__':

    data = [('apple', 100), ('beer', 100), ('pencil', 100), 
        ('beer', 100), ('book', 100), ('apple', 100),
        ('paper', 100), ('pencil', 100), ('orange', 100)]

    sorted_sales = sort_sales(data)
    summary = sales_summary(sorted_sales)
    print(summary)