# 입력받을 학교의 개수 number of Uni int(input())
# 학교랑 술 Uni alcohol = []
# list로 받기
# for 문으로 [i][1] max

Test_Num = int(input())

for j in range(Test_Num):

    Number_of_Uni = int(input())
    Uni_alcohol = []

    for i in range(Number_of_Uni):
        Uni_alcohol.append(input().split())

    print(max(Uni_alcohol[:][1]))

#[:]는 2x2 matrix에서도 통한다 !!!
#split은 문자열 쪼개서 리스트로 만듦