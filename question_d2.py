


#1. Ask  for the user's first name and display the output message  Hello [First Name]

# first_name = input("Enter your first name:")
# print(f"Hello {first_name}")

#2.  Ask the user's first name and then ask for their surname and dispaly the output msg

# first_name = input("Enter your First name: ")
# sur_name = input("Enter your Sur name: ")
# print(f"Hello {first_name} {sur_name}")

#3. write the code that will display the joke "What do you call a bear with no teeth?" and on the next line display the answer  "A gummy bear!"Try to create it using only one line of code

#print("What do you call a bear with no teeth ?\n A gummy bear!" )

#4. There are 2204 pounds in a kilogram.Ask the user to enter a weight in kilograms and convert it to pounds.
# weight_kg =  int(input("Enter the weight: "))
# pounds=weight_kg * 2204
# #pounds = weight_kg * 2.20462
# print(f" The result is {pounds}")

# 5 convert from fahrenheit to celcius
# fahrenheit = int(input("Enter the fahrenheit:"))
# celcuis = (fahrenheit - 32) / 1.8
# print(f" The celcuis temparture is {celcuis}")

# 6 wap to find the bmi

# height_cm = float(input("Enter the height: "))
# weight_kg = int(input("Enter the weight: "))
# bmi = weight / (height ** 2)
# print(f" The BMI result is {bmi}")




#. 7 wap to find the simple interest
#  simple interest = (principal *Rate of interest * tenure)/100

# principal_amount = float(input("Enter the principal amount: "))
# rate_of_interest = float(input("Enter the rate of interest: "))
# tenure_amount = float(input("Enter the tenure: "))
# simple_interest = (principal_amount * rate_of_interest * tenure_amount)/100
# print(f"The simple interest is {simple_interest}")



#8. wap to find the compound interest.
# compound_interest = p *(1 + r/100)^T - p

# p = int(input("Enter the amount: "))
# r = int(input("Enter the interest: "))
# T = int(input("Enter the tenure: "))
# compound_interest = p * ((1 + r / 100) ** T) - p
# print(f" The result is {compound_interest}")

#9 wap to calculate the total marks and percentage of student based on marks in five subjects

# english_marks = int(input("Enter the marks of English: "))
# hindi_marks = int(input("Enter the marks of Hindi: "))
# physics_marks = int(input("Enter the marks of Physics: "))
# maths_marks = int(input("Enter the marks of Maths: "))
# chemistry_marks = int(input("Enter the marks of Chemistry: "))
# Total_marks =english_marks+hindi_marks+physics_marks+maths_marks+chemistry_marks
# print(f"The total mark is {Total_marks}")
# max_marks = 500
# percentage = (Total_marks/max_marks)* 100
# print(f"The mark  percentage of five subject is {percentage}")


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   CONDITIONAL STATEMENTS......>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#wap to check whether a person is eligible for vote or not

# n = int(input("Enter your age: "))

# if n >= 18:

#     print(f"{n} is eligible for vote")

# else:

#     print(f"{n} is not eligible for vote")    

#wap to check whether a number is divisible by 7 or not

# n = int(input("Enter a number: "))

# if n % 7 == 0:
#     print("it is divisible")

# else:

#     print("it is not divisible")    



#wap to display "hello" if a number is entered by user is a multiple of five otherwise print "Bye"

# n = int(input("Enter a number: "))

# if n % 5 == 0:
#     print("Hello")
# else:
#     print("bye")    
 

#wap to display the last digit of a number

# num  = int(input("Enter a number: "))

# print("Last digit of a number is",(num % 10))


#wap to check  whether the last digit of a number is divisible by 3 or not

# num = int(input("Enter a number: "))

# n = num % 10

# if n % 3 == 0:

#     print(f"The last digit is divisible by 3")

# else:

#     print("it is not divisible by 3")    


# wap to accept percentage from user  and display the grades

# > 90  A
# > 80 and <= 90 B
#  >=60 and < 80  c
# < 60 D


# mark = int(input("Enter the mark: ")) 

# if (mark >90):
#     print("your grade is A")

# #elif mark > 80 and mark <= 90: 
# elif 80 <= mark < 90:
#     print("your result is B")


# #elif  60 <= mark < 80:
# elif mark >= 60 and mark < 80:
#     print("your result is C")    

# else:
#     print("your result is D")   



# per = int(input("Enter the percentage: "))
# # perc = (per *500) // 1000

# if per > 90:
#     print(f"your grade is A")

# elif  per > 80 and per <= 90:
#     print(f" your grade is B")   

# elif per  >= 60 and per < 80:
#     print(f"your grade is C")
# else:
#     print(f"your grade is D")



# wap to check whether an year is leap year or not


# yr = int(input("Enter a year:"))

# if( yr % 100 == 0 and yr % 400 == 0) or (yr % 100 != 0 and yr % 4 == 0):

#     print(f"{yr} is leap year")

# else:

#     print(f"{yr} is not a leap year")    


 #wap to find the largest even among 3 numbers.

# num1 = int(input("Enter a number: "))

# num2 = int(input("Enter a nnumber: "))

# num3 = int(input("Enter a number: "))

# max_even = 0

# if num1 % 2 == 0 and num1 > max_even:

#  max_even = num1

# if num2 % 2 == 0 and num2 > max_even:

#     max_even = num2

# if num3 % 2 == 0 and num3 > max_even:

#     max_even = num3        

# if max_even > 0:

#     print(f"{max_even} is largest")

# else:

#     print("get out")     




# #wap to get the last element from  string  enter by user 


# name = input("Enter your name: ")

# print(name[-1])

#print(name[2])

#wap to enter the first name and last name .join them with a space between and print and also print the length'

# f_name = input("Enter your name: ")

# l_name = input("Enter your name: ")

# print(f"{f_name} {l_name}")

# temp = f_name + " " + l_name

# print(temp)

# print(len(temp))


#wap to capatilaze the string


# name = input("Enter a word: ")

# print(name.capitalize())

#wap to get the last element from  string  enter by user

# name = input("Enter a word:")


# print(name[-1])

# print(name[0:5])

# print(name[4:])

# print(name[ ::-1 ])



#wap to enter the first name and last name .join them with a space between and print and also print the length


# f_name = input("Enter your name: ")

# l_name = input("Enter your last name: ")

# print(f"{f_name} {l_name}")

# full_name = f_name + " " + l_name

# print(full_name)

# print(len(full_name))

# print(full_name[:: -1])

# print(full_name[ 1])

# print(full_name.capitalize())

# wap to find  a number is positive,negative or zero and number is less than 10 print hai else print getout

# wap to print odd number from 1 to 30

# i = 1

# while (i <= 30):

#     if(i % 2 != 0):

#      print(i)

#     i = i + 1

# wap to print numbers divisible by 3 and 5 from 1 to 100


# i = 1

# while(i <= 100):

#     if(i % 3 == 0 and i % 5 == 0):

#         print(i)

#     i = i + 1


# wap to find the sum of digits enter by user

# num = 123455

# i = 0

# sum = 0

# num = str(num)

# while(i<len(num)):

#     sum = sum + int(num[i])

#     i = i + 1

# print(sum)



 # wap to find the sum of digits enter by user


num = int(input("Enter a number: "))


i = 0

sum = 0


num = str(num)

while i < len(num):

    sum = sum + int(num[i])

    i = i + 1

print(sum)    