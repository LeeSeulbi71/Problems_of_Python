#최대공약수와 최대공배수

# N1, N2 = map(int, input().split())

# #최대공약수
# for i in range(1, min(N1, N2)+1):
#     if (N1%i==0) and (N2%i==0):
#         greatest_common_factor = i

# #최소공배수
# for j in range(N1*N2, 0, -1):
#     if (j%N1==0) and (j%N2==0):
#         least_common_multiple = j

# print(greatest_common_factor)
# print(least_common_multiple)

##########################################시간 초과............

#유클리드 호제법

n1, n2 = map(int, input().split())

#최대공약수
N1, N2 = n1, n2
if(N2>N1): N1, N2 = N2, N1

while(N2!=0):
    N1 = N1%N2
    N1, N2 = N2, N1

print(N1)

#최대공배수: N1*N2/최대공약수

print(int(n1*n2/N1))