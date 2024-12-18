
# wap to print the greatest elemnt using function

# numbers = [4,6,8,9,2,4,5]


def greatest(numbers):

    max = 0

    for i in numbers:

        if i > max:

            max = i 

    return(max)        

print(greatest([4,6,8,9,2,4,5]))   

# if we use print output shows None use  return for function 