
# harshad number is an integer that is divisible by the sum of its digits
# ex: 9 + 9 = 18 and 18 is divisible by 9

n = 18


temp = n

sum = 0

while n > 0:
    
    digit = n % 10

    sum += digit

    n = n // 10

if temp % sum == 0:              
    
    print("it  is harshad")
    
else:
    
    print("get out")


   