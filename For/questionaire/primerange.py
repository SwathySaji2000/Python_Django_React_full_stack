# wap to print prime number in a given range from 1 to 10.


for j in range(1,10):  # we are using j variable for enter the given range by question.

    if j > 1:

        for i in range(2,j):

            if j % i == 0:

                print(f"{j} is not a prime number")

                break
        else:

                print(f"{j} is a prime number")

    else:

         print("prime number should be greater than one")            


