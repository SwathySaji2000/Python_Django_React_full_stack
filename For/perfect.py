# wap to find a number is perfect number


n = 20

sum = 0

i = 1

for i in range(1,n):

    if n % i == 0:
 
       sum += i
  


if sum == n:

    print(f"{sum} is a perfect number")

else:

    print("get out")    




    