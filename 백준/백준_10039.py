# 평균 점수

# 만약 40점 미만이면 40점

test_score = []

for score in range(5):
    score = int(input())
    test_score.append(score)

sum_test_score = 0
for score in test_score:
    if score < 40:
        sum_test_score += 40
    else:
        sum_test_score += score

print(int(sum_test_score/5))