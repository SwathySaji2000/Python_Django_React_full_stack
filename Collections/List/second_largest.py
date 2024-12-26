

# wap to print the second largest element from the list.

numbers =  [1,2,3,4,5,7]


largest = numbers[0]

second_largest = numbers[1]


for i in numbers:

    if i > largest:

        second_largest = largest

        largest = i


    elif  i < largest and i > second_largest:

        second_largest = i


print(f" The second largest is : {second_largest}")    
