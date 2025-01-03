


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


# keys= [1,2,3,4,5]
# values = [6,7,8,9,10]

# items = {}

# for i in range(len(keys0)):

#     items[keys[i]] = values[i]

# print(items)    


################# LIST comprehension

# items = ["apple","grape","kiwi"]

# new = [i for i in items if "a" in i]
# print(new)

# items = ["12.7",7,2,4,5,"True"]

# new = [ i for i in items if type(i) == int]

# print(new)

# numbers = [1,2,3,4,5,6,7,1,4,1,3,3,4,4,4,4,4,2]

# d = {}

# for i in numbers:

#     d[i] = numbers.count(i)

# print(d)

# wap to find the index of smallest element in the list..


# numbers = [5,8,3,90]

# n = [numbers.index(min(numbers))]

# print(n)


















