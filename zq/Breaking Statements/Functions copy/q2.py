# given two integers return true if the sum of the integers is 20 or if one of the integers is 20. if not, return false.


num1 = int(input("Enter a number: "))

num2 = int(input("Enter a number: "))

sum = (num1  + num2)

if sum == 20 or num1 == 20 or num2 == 20:

    print ("True")

else:

    print("False")    