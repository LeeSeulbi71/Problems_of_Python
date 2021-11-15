#Baseball

Test_num = int(input())

for game in range(Test_num):
    Yonsei_score_list = []
    Korea_score_list = []

    for one_game in range(9):

        Yonsei, Korea = map(int, input().split())
        Yonsei_score_list.append(Yonsei)
        Korea_score_list.append(Korea)

    if sum(Yonsei_score_list) > sum(Korea_score_list):
        print("Yonsei")
    elif sum(Yonsei_score_list) < sum(Korea_score_list):
        print("Korea")
    else:
        print("Draw")