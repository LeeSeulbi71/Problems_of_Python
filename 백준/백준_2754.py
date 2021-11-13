#학점 계산

score = (input())

if score == 'A+':
    grade = 4.3
elif score == 'A0':
    grade = 4.0
elif score == 'A-':
    grade = 3.7
elif score == 'B+':
    grade = 3.3
elif score == 'B0':
    grade = 3.0
elif score == 'B-':
    grade = 2.7
elif score == 'C+':
    grade = 2.3
elif score == 'C0':
    grade = 2.0
elif score == 'C-':
    grade = 1.7
elif score == 'D+':
    grade = 1.3
elif score == 'D0':
    grade = 1.0
elif score == 'D-':
    grade = 0.7
else:
    grade = '0.0'

print(grade)
