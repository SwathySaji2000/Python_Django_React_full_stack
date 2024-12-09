
#  wap to print prime number or not.

# Prime number is a number which is divisible by 1 and that number itself...  

#  start range is  2


number = int(input("Enter a number: "))

while number <= 1:

    print("Enter a value greater than one")

    number = int(input("Enter a number: "))

for i in range(2,number):

      if number % i == 0:

        print("it is not a prime number")

        break

      else:

       print("it is a prime number")




          