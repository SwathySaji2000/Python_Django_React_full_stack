# find the factorial of a number



def factorial(num):

    
   fact = 1

   for i in range(1,num + 1):

        fact = fact * i

        i += 1

   return fact

num = int(input("Enter the num : "))

print(f"The factorial of {num} is {factorial(num)}")


