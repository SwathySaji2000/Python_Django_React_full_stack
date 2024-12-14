# wap to find a number is a harshad or not


number = 156

sum = 0

for i in str(number):  # converts to str 

    sum = sum + int(i)    

print(sum)


if  number % sum == 0:

    print("it is a harshad number")

else:

    print("it is not a harshad number")    