

#  Write a function  that takes an integer n and returns its reverse.
#  Example: reverse_integer(1234) should return 4321.


def rev(number):

    rev = ""

    for i in str(number):

        rev = i + rev

    print(rev)    

rev(1234)    
