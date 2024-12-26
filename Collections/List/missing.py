

# wap to find the missing number in the sequence of numbers in the list

numbers = [ 1,4,2,5,7,6]    # here the missing number is 3


for i in range(min(numbers),max(numbers)):

    if i not in numbers:

        print(i)


