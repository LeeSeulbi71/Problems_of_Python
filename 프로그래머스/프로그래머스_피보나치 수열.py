#재귀 함수를 써야할 것 같은 느낌적인 느낌

def solution(n):
    return Fibonacci(n) % 1234567

def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(4))
print(solution(3))