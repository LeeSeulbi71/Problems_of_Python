# 홀수면 (n-1)/2 * 수박 + 수
# 짝수면 n/2 *수박
def solution(n):
    if n%2 != 0:
        return "수박" * int((n-1)/2) + '수'
    else:
        return "수박" * int(n/2)

print(solution(4))

# 다른 사람 풀이

def water_melon(n):
    return "수박" * (n//2) + "수" * (n%2)
