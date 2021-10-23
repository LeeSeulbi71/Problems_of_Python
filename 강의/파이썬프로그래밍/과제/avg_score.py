def main():
    #===== write your code below =======
    # 계속해서 값들을 입력 받아야 함
    # 만약 입력을 마치고 싶을 때는 0 이하, 100이상의 숫자를 입력함
    # 평균 점수를 내서 화면에 출력
    # 평균점수: 소수점 아래 둘째자리까지
    # 리스트 선언
    # while 반복문
    # 입력 및 리스트에 저장
    # 받은 값들 평균 내기
    # if - break 쓰기

    all_score = []
    
    while 1:
        score = float((input("Give your score (0~100): ")))
        all_score.append(score)
        
        if (score < 0) or (score > 100):
            break
    
    avg_score = sum(all_score[:-1]) / (len(all_score)-1)
    print("Average score is {:.2f}.".format(avg_score))

if __name__ == '__main__':
    main()