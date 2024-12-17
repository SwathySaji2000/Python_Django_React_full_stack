
# is a positive integer where the sum of the factorials of its digits is equal to the number itself.

# factorial : The product of all positive integers up to a number.  factorial of 4 is 4 *3*2*1 = 24

# 145 = 1! + 4!+ 5!


number = 145

sum = 0



for i in str(number):

    fact = 1

    for j in range(1,int(i)+1):    # 1!  

        fact = fact * j            # fact stores the value of factorial

    sum = sum + fact                 # sum keeps the fact value and adding 


if sum == number:

    print(f"{number} is a strong number")  

else :

    print("get out")   
