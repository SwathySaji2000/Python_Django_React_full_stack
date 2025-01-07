


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


#### lamba


# square = lambda n: n**2

# print(square(5))

# wap to find the smallest amoung 3 numbers

# smallest = lambda a,b,c : a if (a > b and a > c) else b if (b>c and b>a)  else c

# print(smallest)
# wap length  of a string

# length = lambda text:len(text)

# print(length("hello"))

# wap to find the max of a number

# maximum = lambda a,b: a if a>b else b

# print(maximum(9,12))

# number = lambda n:"even" if n % 2 == 0 else "odd"

# print(number(9))


# wap to find the numbers divisible by 5

# numbers = [1,3,5,10,4,7,25,30]

# result = list(map(lambda a : a if a % 5 == 0 else None, numbers))
# print(result)


# wap to find the number is positive or negative

# number = [1.4,2,3,-1,-3,-8]

# result = list(map(lambda a : a if  (a > 0  and type(a)==int) else None,number))

# print(result)


###########********************  FILTER

# numbers = [2,5,6,7,10,15,20,25]

# result =list(filter(lambda n: n if n % 5 == 0 else None,numbers))

# print(result)

################## reduce

# from functools import reduce

# numbers =[10,12,3,4,50]

# # result = reduce(lambda a,b:a+b,numbers)
# # print(result)

# result =  list(filter(lambda a:a%2==0,numbers))
# print(result)

# show = reduce(lambda a,b:a+b,result)
# # print(show)

# file = open("j.txt","r")

# print(file.read())

# file = open("h.txt","w")

# file.write("python django")

# file = open("C:/Users/swath/OneDrive/Desktop/fullstack/Breaking Statementss/lol.txt","w")
# file.write("Enjoy each moment")


# create a new file "python.txt" and write " python is object oriented"

# read the content from python.txt and dispaly  and append " programming language"

# file = open("v.txt","w")
# file.write("python is object oriented")
# file.close()

# file = open("v.txt","r")
# print(file.read())

# file = open("v.txt","a")
# file.write(" programming language")
# file.close()

# file = open("v.txt","r")
# print(file.read())



#   create a new file and write " python is a programming language practise it"


# read the words from above which starts with letter "p" and display in a list

# file = open("po.txt","w")

# file.write("python is a programming language practise it")

# file.close()

# result = []

# file = open("po.txt","r")

# # print(file.read())

# # print(file.read().split( " "))

# for i in file.read().split(" "):
#     if "p" in i and i.index("p") == 0:

#         result.append(i)

# print(result)        

items = ["hello","python","hello","django"]

# create a file and write this list to it

# read the file and display the unique elements


file = open("t.txt","w")
for i in items:
  file.write(i + "\n")

list = [ ]

file = open("t.txt","r")

for i in file.readlines():
  
   list.append(i.strip("\n"))

print([ i for i in list if list.count(i) == 1])   

print([ i for i in list  if list.count(i) == 1])