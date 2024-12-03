# wap to find the armstrong of a number


number = 121

temp = number  # stores the original value for futher looping or checking armstrong which simplifies last

length = len(str(number))   # we want  to know the length of a number that  is the power of given number   length = 3

sum = 0

while number > 0:    # checking the condition given number is greater than 0   153 > 0

    digit = number % 10   # we need to get the last digit so dividing the given number by 10  i.e 153 % 10 = 3

    sum += digit ** length  # loop process continues sum stores the digit value and power of length of given number  

    number = number // 10   # by floor division we need to  get the exact value 


print(sum)   


if sum == temp:

    print("it is an armstrong number")

else:

    print("it is not an armstrong number")    



