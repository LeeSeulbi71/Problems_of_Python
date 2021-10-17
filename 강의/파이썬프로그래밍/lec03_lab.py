# 본 프로그램은 섭씨를 화씨로 변환해주는 프로그램

print("본 프로그램은 섭씨를 화씨로 변환해주는 프로그램입니다.")
C_temperature = float(input("변환하고 싶은 섭씨 온도를 입력해 주세요: \n"))

F_temperature = (9/5 * C_temperature) + 32

print("섭씨 온도: {:.2f}".format(C_temperature))
print("화씨 온도: {:.2f}".format(F_temperature))