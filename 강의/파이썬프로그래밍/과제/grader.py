
def compute_average(*score):
    """점수들을 인자로 받아 평균 점수를 계산하는 함수입니다.

    Input:
        args: 0점 이상 100점 이하의 점수들 (가변인자)
    
    Output:
        average: 평균 점수
    
    Examples:
        >>> compute_average(10,20,30)
        20.0
        >>> compute_average(60,54,82,100)
        74.0
        >>> compute_average(60,120)
        Invalid score!
    """
    # 100이 넘지 않을 때만 average를 계산하도록 해야함
    # 100이 넘는지 하나하나 검사
    # 100이 넘으면 바로 빠져나옴
    # print(Invalid score!)
    #===== write your code below =======
    bool_value = []
    for i in score:
        bool_value.append(str((i > 100 or i < 0)))

    if 'True' in bool_value:
        average = print("Invalid score!")
    else:
        average = sum(score) / len(score)
    
    #===================================
    
    return average

def print_grade(average):
    """평균 점수를 입력받아 해당되는 grade를 화면에 출력하는 함수입니다.

    Input:
        average: 평균 점수

    Examples:
        >>> get_grade(90.0)
        Average: 90.0000
        Grade: A
        >>> get_grade(62.4)
        Average: 62.4000
        Grade: D
    """
    #===== write your code below =======

    if average >= 90:
        Grade = 'A'
    elif (average>= 80) & (average <90):
        Grade = 'B'
    elif (average>= 70) & (average <80):
        Grade = 'C'
    elif (average>= 60) & (average <70):
        Grade = 'D'
    else:
        Grade = 'F'     

    print("Average: {:.4f}".format(average))
    print("Grade:", Grade)
    #===================================


if __name__ == '__main__':

    print('Test...')
    average = compute_average(10, 20, 30)
    print_grade(average)
