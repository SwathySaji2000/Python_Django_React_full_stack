# wap to find the second largest number


num1 = int(input("Enter a value: "))

num2 = int(input("Enter a value: "))

num3 = int(input("Enter a value: "))


# num1 = 2 , num2 = 4, num3 =6

#(2 > 4 and 2 < 6)  or (2 < 4 and 2 > 6)  # true or true is true

if(num1 > num2 and num1 < num3)  or (num1 < num2 and num1 > num3):    

    print(f"{num1} is second largest")


elif(num2 > num1 and num2 < num3) or  (num2 < num1 and num2 > num3):

    print(f"{num2} is second largest")


else:

    print(f"{num3} is second largest")    