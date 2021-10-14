#계약조항: a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와!
#무슨 이런 계약이 있지?
# 0층, 1호
# 2차원 배열
# apartment [0,0] = 0층 1호
# 중첩반복문

T = int(input())

for i in range(T):

    apartmant = [[ 0 for i in range(14)] for j in range(20)]

    for i in range (1, 15):
       apartmant[0][i-1] = i

    for j in range (1, 20):
        for k in range (1,15):
            for n in range (0, k):
                apartmant[j][k-1] += apartmant[j-1][n]

    a = int(input())
    b = int(input())

    print(apartmant[a][b-1])

# 제출하고 나서야 apartment를 apartmant로 쓴 걸 알았당 ~~~
# 어떻게 일관성 있게 스펠링을 틀리지?
# 여튼 맞아서 기분 좋음