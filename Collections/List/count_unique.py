
# define a function which should return the count of unique numbers in a list
# also if an element is repeating print the element and the number of times is repeating

# numbers = [1,2,4,5,6,7,2,1,4,4,4]



def unique(numbers):
   
    count = 0

    for i in numbers:

     if numbers.count(i) == 1:

        count += 1


     elif numbers.count(i) > 1:   

      print(f"The element is {i} = occurs {numbers.count(i)} times")

     print(count)

unique([1,2,3,3,5,6,6,7])   
          