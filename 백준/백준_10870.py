def Fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n + Fibonacci(n-1)

n = int(input())
print(Fibonacci(n))