
#  wap for ugly number [2,3,5]

 
number = 10

for i in [2,3,5]:

    while (number%i == 0):   # 10%2==5, we need to divide the number until we get an answer to 1 

        number = number / i


    if number == 1:

            print("it is an ugly number")
            break

else:

     print("if is not a ugly number")            







