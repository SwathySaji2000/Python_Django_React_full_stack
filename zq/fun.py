


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


# file = open("t.txt","w")
# for i in items:
#   file.write(i + "\n")

# list = [ ]

# file = open("t.txt","r")

# for i in file.readlines():
  
#    list.append(i.strip("\n"))

# print([ i for i in list if list.count(i) == 1])   

# print([ i for i in list  if list.count(i) == 1])


# with open("po.txt","r+") as file:
#   print(file.read())
#   file.write(" hiiis")
# #   print(file.read())

# with open("p3.txt","w+") as file:
#    print(file.read())
#    file.write("hjisghghs")


# try:
#      a = int(input("Enter a number: "))

#      b = int(input("Enter a number: "))

#      result = a/b

#      print(result)

# # except:
     
# #      print("zero is not divisible")


# # try:
    
# #     a = int(input("Enter a number: "))

# #     b = int(input("Enter a number: "))

# #     result = a/b
# #     print(result)


# # except ZeroDivisionError:

# #     print("it is not divisible by zero")

# # except ValueError:
    
# #     print("enter a digit")


# # open a file and read  if the file content in this directory  from console 
# # otherwise print "sorry file is not exisitng in this directory"  using try n except+

# # try:
    
# #     with(open(input("Enter the file name:"))) as file:
        
# #         print(file.read())

# # except FileNotFoundError:

# #     print("sorry file is not exisitng in this directory")            




# # numbers = [1,23,45,67,80,10]

# # try:
    
# #     print(numbers.index(int(input("Entera value: "))))


# # except ValueError:
    
# #     print("please enter a value")

# # except  NameError:

# #     print("Enter a valid digit")   


# # suppose an array of length n sorted  in ascending order is rotated between 1 and n times.

# # ex the array numbers 


# # num = [1,3,4,6,7,8,9]

# # n=int(input("Enter the number of rotations: "))

# # for i in range(n):
# #   num.insert(0,num.pop())

# # print(num) 

# #wap to find ugly number

# number = 19

# for i in [2,3,5]:

#     while number%i==0:
#      number = number / i

#     if number == 1:
#         print("it is an ugly number")
#         break

# else:
#        print("it is not  an ugly number")
          





################ regex

# import re 


# license = "my car number is kl05am5962"

# pattern = r'kl[0-9]{2}[A-z]{2}[0-9]{4}'

# matcher = re.finditer(pattern,license)

# for i in matcher:

#     print(i.start(),i.end())

import re
# text = "Python Is a Programming language"



# pattern = r'[A-Z][a-z]*'

# matcher = re.findall(pattern,text)

# print(matcher)



# # wap to find the date format

# text = "23-04-2020"

# pattern = r'(0[0-9]1[0-9]2[0-9]3[0-1])-(0[0-9]1[0-2])-(\d{4})'

# matcher = re.findall(pattern,text)

# print(matcher)

# import re

# text = "PLTPS0589W"

# pattern = r'\b[A-Z]{5}[0-9]{4}[A-Z]{1}'

# matcher = re.findall(pattern,text)

# print(matcher)

# import re

# # wap to validate mail id

# text = "swathysaji123@gmail.com"

# pattern = r'\b[A-z0-9#]+@[a-z]*+.[a-z]{2,}'


# matcher = re.findall(pattern,text)

# print(matcher)

#***************************8 Functions 


# wap to add 2 numbers


# def subract(a,b):
    
#     s = b-a
#     print(s)
# subract(5,6)    
    


# def square(a):

#     print(a ** 0.5)

# square(4)    


# def squareroot(num):
#     print(num ** 0.5)
# squareroot(5)    ; / '    `
# 

# def factorial(num):
#     fact = 1

#     for i in range(1,num+1):

#          fact = fact * i
#          i += 1
#     return(fact) 

# num = int(input("Enter the number: ")) 

# print(f"The factorial of {num} is {factorial(num)}")

# find the divisors of a number

# def div(num):

#     for i in range(1,num):

#         if num % i == 0:

#             print(i)   

# div(70)                 

#write a function to check whether the string is pangram.

# "The quick  brown for jumps over the lazy dog" => sentence contain all letters

# from A to Z so its a pangram.



# def pangram(text):

#     letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     letters = letters.lower()

#     for i in letters:

#         if i not in text.lower():

#              print("It is not a pangram")
#              break
        
#         else:
#              print("it is a pangram")
#              break
        
# word = input("Enter the string: ")
# pangram(word)  
#       
# Given a string, return a string for every character in the orginal there are three characters.

# hello == hhheeellllllooo
      
# def dup(text):
#           print(text*3)
# dup("hello")          


# ################## OOPS 


# # class Student:

# #         def details(self,name,course):
                
# #                 self.name = name
# #                 self.course = course
# #                 print(f"Welcome {name}")   

# #         def show_details(self):
# #                 print(f"Hey {self.name} and you got admmision to {self.course}")        

# # obj = Student()
# # obj.details(name="appu",course="BCA")   
# # obj.show_details()             


# class Bank:
#     def user(self,name,ac_type,balance):
#         self.name = name
#         self.ac_type = ac_type
#         self.balance = balance

#         print(f"Welcome to our Bank, heyy {name}")

#     def savings(self,d_ac):
#         #self.d_ac = d_ac
#         print(f"Your current balance is:{self.balance + d_ac} ")    

#     def withdrew(self,w_ac):
#         #self.w_ac = w_ac

#         if self.balance >= w_ac:
#             print(f"Transction Successful ")
#             self.balance -= w_ac
#             print(f"  After withdrawl your current balance is: {self.balance}")
#         else:
#             print("Insufficient balance")        


# obj = Bank()
# obj.user(name="swathy",ac_type="savings",balance=4000)
# obj.withdrew(w_ac=500)
# obj.savings(d_ac=3000)

# #paperdoll
# def paperdoll(text):

#     new = " "
#     for i in text:
#         new += i*3

#     print(new)
# paperdoll("hello")        

# def factorial(n):

#     fact = 1

#     for i in range(1,n+1):
#         fact = fact*i
#         i += 1
#     print(fact)
# factorial(5)        

# class Student:

#     def __init__(self,name,age,mark):
#         self.name = name
#         self.age = age
#         self.mark = mark

# #     def method1(self):
# #         print(f"hey {self.name} and you have {self.mark}")

# #     def method2(self):
# #         print(f"hey {self.name} and your age is {self.age} and you have {self.mark}")

# # obj1=Student(name="swathy",age=23,mark=100)
# # obj2=Student(name="jesty",age=23,mark=190)
# # obj1.method2()
# # obj2.method1()
        
# # crete a class called Mark

# # method1: add marks of 5 subjects of a student and add it to a list

# # method2: display the average of  marks 

# class Mark:

#     def __init__(self,name):
#         self.name = name
#         self.data = []
#         self.details = {}

#     def add(self,*args):
#         for i in args:
#             self.data.append(i)
#         print(self.data)

#     def avg(self):

#         sum = 0

#         for i in self.data:
#             sum += i
#             avg = sum/len(self.data)  
#         print(f"{avg}")   

#         self.details[self.name]  = self.avg

#     def details(self):
#         print(f"{self.details}")       

# obj=Mark(name="achu")

# obj.add(45,56,78,23,40)
# obj.avg()

# def add(*args):

#     sum = 0

#     for i in args:
#         sum += i
#     print(sum)

# add(3,4,5)        
# 
# wap to find the factors of even numbers using function with parameters as args

# def fact(*args):

#     for i in args:

#         if i % 2 == 0:

#             for j in range(1,i):

#                 if i % j == 0:

#                     print(j)                 



# fact(12)
# wap to find the sum of odd n even numbers
# using function

# def number(*args):

#     even_sum = 0
#     odd_sum = 0

#     for i in args:
#         if i % 2 != 0:
#             odd_sum += i
#         else:
#             even_sum += i

#     print(f"Even sum is:{even_sum}")    
#     print(f"Odd sum is : {odd_sum}")     

# number(1,3,5)
# number(8,4,6)    

#create a class and display in a dictonary {'anna': {'age': 23, 'mark': 67}}  

# name, {}

# add mark,age'

# # get mark
# #create a class and display in a dictonary {'anna': {'age': 23, 'mark': 67}}  

# # name, {}

# # add mark,age'

# # get mark  abd updatae


# class Student:
#     def __init__(self,name):
#         self.name = name
#         self.data = {}

#     def add_details(self,mark,age):
#         self.mark = mark
#         self.age = age
#         self.data[self.name] = {"age":age,"mark":mark}
#         print(self.data)


#     def get_mark(self):
        
#         return self.data[self.name].get("mark")  

# #     def get_age(self):
# #         return self.data[self.name].get("age")   
    

# #     def update_details(self,age=None,mark=None):

# #         if age == None:
# #             self.data[self.name][mark]=mark
# #             return self.data
# #         elif mark == None:
# #             self.data[self.name][age]=age
# #             return self.data
# #         else:
# #             self.data[self.name][mark]=mark
# #             self.data[self.name][age]=age
# #             return self.data
        



# # obj = Student(name = "sara")
# # obj.add_details(mark=78,age=23)
# # print(obj.get_mark())
# # print(obj.get_age())
# # print(obj.update_details( ))
        

# class Library:

#     def _init_(self):

#         self.data = {}

#         self.details = []

#     def add_book(self,title,author,year):

#         self.title = title
#         self.author = author
#         self.year = year

#         self.data[title]={"author":author,"year":year} 

#         print(self.data)

#     def remove(self,name):

#         if name in self.data:

#             del self.data[name] 

#             print(self.data)

#         else:

#             print("not found")

#     def get_title(self,years):

#        if years >=2000:

#             self.details.append(self.title)

#             print(self.details)

#        elif years<2000:
#            self.details.append(self.title) 

#            print(self.details)  




# obj = Library() 

# obj.add_book(title="dreams",author='kalaam',year=1999)
# obj.add_book(title="malgudi",author="basheer",year= 1998)

# #obj.remove(name="malgudi")
# obj.get_title(years=2000)

    
    # create a class library

# add_book: parameters title,author,year

# {title:{author:"author",year:"year"}}

# #remove bookname

# # year > 2000 in a list 
# class Library:

#     def __init__(self):

#         self.data ={}
        
#     def add_book(self,title,author,year):
        
#         self.title = title
#         self.author = author
#         self.year = year
#         self.data[self.title]={"author": author,"year":year}

#         print(self.data) 

# obj =Library(title="Hope")
# obj.add_book(author="j.k",year=2300)           
            

# def divisor(num):

#     for i in range(1,num+1):

#         if num % i == 0:

#             print(i)

# divisor(49)

# even factors

# def fact(*args):

#     for i in args:

#         if i % 2 == 0:

#             for j in range(1,i):

#                 if i % j == 0:

#                     print(j)

# # fact(67,16)                    
# def factorial(num):

#     fact = 1

#     for i in range(1,num+1):

#         fact = fact * i

#         i += 1

#     return fact

# num = int(input("Enter the number: "))

# print(f"The factorial of {num} is : {factorial(num)}")
            
# wap to find the sum of odd n even numbers
# using function

# def sum(*args):

#     even_sum = 0
#     odd_sum = 0

#     for  i in args:

#         if i % 2 == 0:

#             even_sum += i

#         else:

#             odd_sum += i

#     print(f"Even sum is: {even_sum}")

#     print(f"Odd sum is: {odd_sum}")                       


# # sum(1,3,4)

# def pangram(text):

#     letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     letters = letters.lower()

#     for i in letters:

#         if i not in text.lower():

#             print(f"{text} is not a pangram")
#             break

#         else:

#             print(f"{text} is a pangram") 
#             break 

# pangram("The quick  brown for jumps over the lazy dog")              













# # Given a string, return a string for every character in the orginal there are three characters.

# # hello == hhheeellllllooo

# def triple(text):

#     new = ""

#     for i in text:

#         new += i*3

#     print(new)

# triple("swathy")

# given three integers between 1 and 11, if their sum is less or equal to 21, retun their sum. 
# if their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# finally, if the sum (even after adjustment ) exceeds 21, return 'BUST'.


# def sum(a,b,c):

#     value = a+b+c

#     if value <= 21:

#         print(value)

#     elif (a == 11 or b == 11 or c == 11) and (value > 21 ):

#         print(value - 10) 


#     if (value - 10) > 21:

#         print("BUST")     


# sum(11,13,14)

# given two integers return true if the sum of the integers is 20 or if one of the integers is 20. if not, return false.


# def sum(n1,n2):
#    n1 = int(input("Enter the number: "))
#    n2 = int(input("Enter the number:"))

#    result = n1+n2



#    if (n1 == 20 or n2 == 20  or result == 20)  and result > 20:

#       print(True)

#    else:
#       print(False)


# sum(n1=3,n2=12)

# wap to find the number is within 10 either 100 or 200, 


# # def find(n):

# #     if (n>=90 and n <= 110) or (n >= 190 and n <= 210):

# #         print(True)


# #     else:

# #         print(False)

# # find(198)       

# # given an string, return true if any value appears at least twice in the string.

# # and return false if every element is distinct. using function.




# def positive(fn):

#     def wrapper():

#         print("Welcome")

#         return fn
    
#     return wrapper()


# @positive

# def greet():

#     print("Hello")

# greet()    

# write a function  for  the sum  of numbers using  decorator


# def positive(fn):

#     def wrapper(*args):

# #         for  i in args:

# #             if i < 0:

# #                 print("Please enter a positive value:")
# #                 break
# #         else:
# #             return fn(*args)
# #     return wrapper

# # @positive

# # def sum(*args):

# #     sum = 0

# #     for i in args:
# #         sum += i

# #     print(sum)

# # sum(3,4,5)        

# def positive(fn):

#     def wrapper(*args):

#         for i in args:

#             if i < 0:

#                 print("Please enter a positive value:")
#                 break
#             else:

#                 return fn(*args)
            
#     return wrapper

                 


# @positive
# def sum1(*args):

#     sum = 0

#     for i in args:

#         sum += i

#     print(sum)       

# sum1(4,5,6)   
       
### Bubble Sort


numbers = [3,6,1,9,7]

n = len(numbers)
for i in range(n):

    for j in range(0,n-i-1):


        if numbers[j] > numbers[j+1]:

            numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
            
print(numbers)            





















    
        