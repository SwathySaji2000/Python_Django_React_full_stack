# given three integers between 1 and 11, if their sum is less or equal to 21, retun their sum. 
# if their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# finally, if the sum (even after adjustment ) exceeds 21, return 'BUST'.


def sum(a,b,c):

    value = a + b + c

    if a + b + c <=21:

        print(a + b + c)

    elif (a == 11 or b == 11 or c == 11) and (a + b + c >21):

        print(value - 10)

    if (value-10)>21:

        print("Bust")

sum(11,11,11)               
























# def sum(num1,num2,num3):
     

#   total_sum = num1+num2+num3
  
#   if total_sum <= 21:

#     return("The result is: {total_sum}")

#   elif total_sum > 21 and 11 in (num1,num2,num3):

#     adjusted_sum = total_sum - 10

#     if adjusted_sum <= 21:
      
#       return adjusted_sum
    
#     else:

#      return ("BUST")
    
#   return("BUST")  

# num1 = int(input("Enter a number: "))

# num2 = int(input("Enter the second number: "))

# num3 = int(input("Enther the third number: "))

# result = sum(num1, num2, num3)

# print(f"The result is: {result}")
   



