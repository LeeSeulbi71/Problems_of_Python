#Yangjojang of The Yeear

Test_Num = int(input())

for i in range(Test_Num):

    Number_of_Uni = int(input())
    Uni_alcohol_list = []

    for Uni in range(Number_of_Uni):
        One_Uni = list(map(str, input().split()))
        Uni_alcohol_list.append(One_Uni)
    
    for number in range(len(Uni_alcohol_list)):
        Uni_alcohol_list[i][1] = int(Uni_alcohol_list[i][1])

    for j in range(Number_of_Uni):
        print(type(Uni_alcohol_list[j][1]))
    
    #sorted_Uni_alcohol = sorted(Uni_alcohol_list, key= lambda x: x[1], reverse = True)

    #
    # print(sorted_Uni_alcohol, sorted_Uni_alcohol[0][0])