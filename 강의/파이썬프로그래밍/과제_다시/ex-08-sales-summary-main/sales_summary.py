
def sort_sales(data):
    #===== write your code below =======
    sum_data = []

    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i][0] == data[j][0]:
                sum_data.append((data[i][0], data[i][1]+data[j][1]))
    for n in range(len(data)):
            if data[n][0] not in set([sum_data[k][0] for k in range(len(sum_data))]):
                sum_data.append((data[n][0], data[n][1]))
    
    sum_data.sort(key=lambda x: x[1], reverse=True)                    
    
    return sum_data
def sales_summary(data):
    #===== write your code below =======
    final = []
    for i in range(len(data)):
        final.append(data[i]+(i+1,))
    
    return final

if __name__ == '__main__':

    data = [('apple', 5), ('beer', 2), ('pencil', 1), 
            ('beer', 2), ('book', 8), ('apple', 9),
            ('paper', 3), ('pencil', 13), ('orange', 6)]

    sorted_sales = sort_sales(data)
    summary = sales_summary(sorted_sales)     
    print(summary)