# find the divisors of a number

def divisor(num):

    for i in range(1,num):

        if num % i == 0:

            print(i)

divisor(49)         