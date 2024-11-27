# wap to find the second smallest among 3 numbers


num1 = int(input("Enter a value: "))

num2 = int(input("Enter a value: "))

num3 = int(input("Enter a value: "))

if (num1 > num2 and num1 < num3) or (num1 < num2 and num1 > num3) :

    print(f"{num1} is second smallest")


elif (num2 > num1 and num2 < num3) or (num2 < num1 and num2 > num3):

    print(f"{num2} is second smallest") 


else:

    print(f"{num3} is second smallest")       


