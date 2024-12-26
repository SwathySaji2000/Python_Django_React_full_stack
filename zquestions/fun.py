


# define a function which should return the count of unique numbers in a list
# also if an element is repeating print the element and the number of times is repeating..



# def unique(numbers):

#     count = 0

#     for i in numbers:

#         if numbers.count(i) == 1:

#             count += 1

#         elif numbers.count(i) > 1:
             
#          print(f"{i} = {numbers.count(i)}")  

#     print(count)         

# unique([1,2,3,3,5,6,7])   



#  define a function which should return true if list contains atleast one duplicate element

#else return false


# def duplicate(numbers):

#     for i in numbers:

#        if numbers.count(i) > 1:

#         return(True)

#        else:

#         return(False)

# print(duplicate([2,5,6,2,7,8]))  


# wap to print the greatest element using function

# numbers = [4,6,8,9,2,4,5])

# def greatest(numbers):

#     max = 0


#     for i in numbers:

#         if i > max:

#             max = i
#     return(max)    

# print(greatest([4,6,8,9,2,4,5]))    




#  read numbers from the user until user enters a value 0
#  then display the list of numbers in ascending order

  
# n = int(input("Enter a number: ")) 
    
# num = []

# while(n != 0):
    
#     num.append(n)

#     n = int(input("Enter a number: "))

#     print(f"{n} is addedd")

#     num.sort()

# print(num)    



# # wap to print the smallest number using function
# def smallest(numbers):

#   small = numbers[0]

#   for i in numbers:

#     if i < small:
      
#       small = i

#       print(i)

# smallest([13,4,7,8])      
                

 # wap to interchange first and last elements of a list...

# numbers = [16,58,78,29] 

# if (numbers):
#    numbers[0],numbers[-1] = numbers[-1],numbers[0]
#    print(f"{[numbers[0]]} , {[numbers[-1]]}")

# else:
   
#    print("empty list")

# wap to swap the element 

# def swap(numbers):
    
#   numbers = [10,20,30,40,50]
#   temp = 0

#   if(numbers):    

#     numbers[0] = numbers[1]

#     numbers[1] = temp

#     temp = numbers[0]

#     print(numbers)

#   else:

#     print("getout")  

# swap([10,20,30,40,50])





# text = "Hello  World"

# word = text.split()

# rev = ""

# for i in reversed(word):
    
#     rev = rev + i + " "

# print(rev)    










