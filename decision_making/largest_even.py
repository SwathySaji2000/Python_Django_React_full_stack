 #wap to find the largest even among 3 numbers.


num1 = int(input("Enter a number: "))

num2 = int(input("Enter a number: "))

num3 = int(input("Enter a number: "))

max_even = 0

if num1 % 2 == 0  and num1 > max_even:

    max_even = num1

if num2 % 2 == 0 and num2 > max_even:

    max_even = num2

if num3 % 2 == 0 and num3 > max_even:

    max_even = num3

if max_even > 0:
  
    print("max_even")  

else:

    print("get out")    