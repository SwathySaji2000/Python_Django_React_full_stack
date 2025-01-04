

# wap to find the factors of even numbers using function with parameters as args


def fact(*args):

    result = 0

    for i in args:

        if i % 2 == 0:

            for j in range(1,i):

                if i % j == 0:

                    print(j)   

fact(16)                      

fact(8,9,65)
                

           

    

     



