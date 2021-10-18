def solution (a,b):
    num = []
    if a > b:
        temp = a
        a = b
        b = temp
    for i in range(a,b+1):
        num.append(i)
    return sum(num)

print(solution(5,3))

#다른 사람 풀이

def adder(a,b):
    if a > b: a, b = b, a
    return sum(range(a,b+1))

    #굳이 for로 리스트 만들 필요 없음!