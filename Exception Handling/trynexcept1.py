try:

    a = int(input("Enter a number: "))

    b =int(input("Enter a number: "))

    print(a/b)

    

except ZeroDivisionError:

    print("divided by zero is not possible")   

except ValueError:

    print("please enter a digit")     

