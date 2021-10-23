def main():
    #===== write your code below =======
    year = int(input("Give a year: "))
    
    if (year % 4 == 0) & (year % 100 != 0):
        print("The year is a leap year.") 
        
    elif year % 400 == 0: 
        print("The year is a leap year.") 

    else:
        print("The year is not a leap year.")


if __name__ == '__main__':
    main()