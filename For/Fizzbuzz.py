# write a for loop that iterates from 1 to 100. 
# print "Fizz" for multiples of 3.
# print  "Buzz" for mutiples of 5 
# print "FizzBuzz" for multiples of both 3 and 5.


n = int(input("Enter a number: "))

for i in range(1,100):

    if n % 3 == 0  and n % 5 != 0:

        print("Fizz")

        break

    elif n % 5 == 0 and n % 3 != 0:

        print("Buzz")   

        break

   

    elif n % 3 == 0 and n % 5 == 0:

        print("FizzBuzz") 

        break   