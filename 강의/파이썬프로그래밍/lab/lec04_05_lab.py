# 2차원 리스트 처리 - 사람별 평균

kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]

midterm_score_avg = []
midterm_score = [kor_score, math_score, eng_score]

for i in range(5):
    for j in range(3):
        midterm_score_sum = 0
        midterm_score_sum += midterm_score[j][i]
    midterm_score_avg.append(midterm_score_sum / 3)

for i in midterm_score_avg:
    print("평균은 {:.2f} 점입니다.".format(i))
    