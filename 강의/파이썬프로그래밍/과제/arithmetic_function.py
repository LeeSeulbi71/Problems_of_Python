def addition(a, b):
    """두 개의 숫자 a, b를 입력받아 그 합을 출력하는 함수입니다.

    Input:
        a: 숫자 값 (e.g., int or float)
        b: 숫자 값 (e.g., int or float)
    
    Output:
        result: a와 b의 합
    
    Examples:
      >>> addition(3,5)
      8
      >>> addition(3,2)
      5
    """
    #===== write your code below =======

    result = a + b

    #===================================

    return result


def subtraction(a, b):
    """두 개의 숫자 a, b를 입력받아 그 차을 출력하는 함수입니다.

    Input:
        a: 숫자 값 (e.g., int or float)
        b: 숫자 값 (e.g., int or float)
    
    Output:
        result: a에서 b를 뺀 값
    
    Examples:
      >>> subtraction(3,5)
      -2
      >>> subtraction(3,2)
      1
    """
    #===== write your code below =======

    result = a - b

    #===================================

    return result


def multiplication(a, b):
    """두 개의 숫자 a, b를 입력받아 그 곱을 출력하는 함수입니다.

    Input:
        a: 숫자 값 (e.g., int or float)
        b: 숫자 값 (e.g., int or float)
    
    Output:
        result: a와 b의 곱

    Examples:
      >>> multiplication(3,5.1)
      15.3
      >>> multiplication(3,2)
      6
    """
    #===== write your code below =======

    result = a * b

    #===================================

    return result


def division(a, b):
    """두 개의 숫자 a, b를 입력받아 a를 b로 나눈 값을 출력하는 함수입니다.

    Input:
        a: 숫자 값 (e.g., int or float)
        b: 숫자 값 (e.g., int or float)
    
    Output:
        result: a를 b로 나눈 값
    
    Examples:
      >>> division(5,5)
      1
      >>> division(4,2)
      2
    """
    #===== write your code below =======

    result = a / b

    #===================================

    return result

def absolute_value(a, b):
    """두 개의 숫자 a, b를 입력받아 그 차이의 절대값을 출력하는 함수입니다.

    Input:
        a: 숫자 값 (e.g., int or float)
        b: 숫자 값 (e.g., int or float)
    
    Output:
        result: a와 b의 차이의 절대값
    
    Examples:
      >>> absolute_value(4,10)
      6
      >>> absolute_value(3.2,1.1)
      2.1
    """
    #===== write your code below =======

    result = abs(a - b)

    #===================================

    return result


def main():
    print("Addition Test")
    print(addition(3,5)) # Expected Result: 8
    print(addition(10,5) == 15) # Expected Result: True
    print("Addition Test Closed \n")


    print("Subtraction Test")
    print(subtraction(3,5)) # Expected Result: -2
    print(subtraction(10,5) == 5) # Expected Result: True
    print(subtraction(10,15) == 5) # Expected Result: False
    print("Subtraction Test Closed \n")

    print("Multiplication Test")
    print(multiplication(3,5)) # Expected Result: 15
    print(multiplication(10,5) == 50) # Expected Result: True
    print(multiplication(10,-3) == 20) # Expected Result: False
    print("Multiplication Test Closed \n")

    print("Division Test")
    print(division(5,5)) # Expected Result: 1
    print(division(5,4)) # Expected Result: 1.25
    print(division(10,5) == 2) # Expected Result: True
    print(division(10,-3) == 0.33333) # Expected Result: False
    print("Division Test Closed \n")

    print("Absolute Value Test")
    print(absolute_value(1,2)) # Expected Result: 1
    print(absolute_value(4,2.5) == 1.5) # Expected Result: True
    print(absolute_value(-3,5) == 8) # Expected Result: True

if __name__ == "__main__":
    main()
