#if 확인

import math

def solution(n):
    num = math.isqrt(n)
    if pow(num, 2) == n:
        return pow((num+1),2)
    else:
        return -1

print(solution(121))

# 다른 사람 풀이
# 굳이 import math할 필요 없음!

def nextSqure(n):
    sqrt = n ** (1/2)
    print(sqrt)
    if sqrt % 1 == 0:
        return (sqrt+1)**2
    else:
        return -1

print(nextSqure(3))