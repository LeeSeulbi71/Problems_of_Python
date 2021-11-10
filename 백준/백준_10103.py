# 주사위 게임

# 처음 점수: 100점
# 낮은 숫자 = 높은 숫자만큼 점수를 잃음
# 같을 때 = 점수를 잃지 않음

Round_Num = int(input())
Changyeong = 100
Sangdeok = 100

for i in range(Round_Num):
    Changyeong_N, Sangdeok_N = map(int, input().split())
    if Changyeong_N > Sangdeok_N:
        Sangdeok -= Changyeong_N
    elif Changyeong_N < Sangdeok_N:
        Changyeong -= Sangdeok_N 
    else:
        continue

print(f"{Changyeong} \n{Sangdeok}")
        