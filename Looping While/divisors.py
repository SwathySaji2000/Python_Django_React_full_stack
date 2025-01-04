

#wap to find the divisors of a number enter by user

num = int(input("Enter a number: "))

i = 1   # every number is divisible by 1 so intialize with 1

while(i < num):  #never use  <=  the number which is equal to that number we cant use  

    if num % i == 0: # num is divisible by i 

        print(i)


    i = i + 1    