
# wap to find the perfect number   # 6 = 1+2+3

n = int(input("Enter a number:  "))

temp = n

sum = 0 
 
divisor  = 1 


while divisor < n:  

    if n % divisor == 0 :

      sum += divisor

    divisor += 1

if sum == temp:

    print(f"{temp} is a perfect number") 

else:

    print(f"{temp} is not a perfect number")       







        




