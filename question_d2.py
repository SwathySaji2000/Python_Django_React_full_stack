


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


# num = int(input("Enter a number: "))


# i = 0

# sum = 0


# num = str(num)

# while i < len(num):

#     sum = sum + int(num[i])

#     i = i + 1

# print(sum)    



# wap to find the product of number enter by user


# num = int(input("Enter a number: "))

# i = 0 

# prod = 1

# num = str(num)

# while(i <len(num)):

#     prod = prod * int(num[i])

#     i = i + 1

# print(prod)    


# write a program to print frt 10 even numbers and frst 10 odd numbers


# i = 0

# even = 0

# while (i < 10):

#     if i % 2 == 0:

#         even = even + i

#     i = i + 1

# print(f"The first even numbers are: {even}")        


# wap to print the leap years from 

# start_limit = 1900

# end_limit = 2024

  


# wap to print sum of elements in odd index

# num = 145637  # 4 + 6 + 7

# i = 0

# num = str(num)

# sum = 0

# while (i < len(num)):

#     if ( i % 2 != 0):

#         sum = sum + int(str(num)[i])

#     i = i + 1

# print(sum)    

# wap to find the armstrong of a number.

# 121 i.e 1^3 + 2^3 + 1^3

# num = 121

# temp = num


# length = len(str(num))

# sum = 0

# while (num > 0):

#     digit = num % 10

#     sum  += digit  ** length

#     num = num // 10

# print(sum)    


#palliandrome

# num = 121

# temp = num

# rev = 0

# while (num > 0):

#     digit = num % 10

#     rev = rev * 10 + digit

#     num = num // 10

# print(rev)    

# if temp == rev:

#     print("it is a palliandrome")

# else:

#     print("it is not a palaiandrome")    



# set the total to 0 to start with. while the total is 50 or less, ask the user to input a number. 
# Add that number to  the total and print the message " The total is.. [total]"
# stop the loop when the total is over 50.


# total = 0

# while ( total <= 50):

#     num =int(input("Enter a number: "))

#     total += num

# # print(f"The total  is {total}")    


# # create a variable called compnum and set the value to 50. ask the user to enter a number. while their guess is not the same as the
# # compnum value, tell them if their guess is too low or too high and ask them to have another guess.
# # # if they enter the same value as compnum display the message "well done, you took [count] attempts".

# # compnum =50

# # count = 0
# # num = 0

# # while num != compnum:

# #     num = int(input("Enter a number:"))

# #     count += 1

# #     if num > compnum:

# #      print("too high")

# #     elif num < compnum:

# #      print("too low")    

# # print(f"Well done, you took {count} times")     


# # ask the user to enter a number between 10 and 20 .if they enter a value under 10, display the message "too low" and ask them to try again.
# # if they enter a value above 20,  display the message "too high " and ask them to try again.  keep  repeating this until enter a value 
# # that is between 10 and 20 and then display the message "Thank you."

       
# # n = int(input("Enter a number:  "))


# # while n < 10 or n > 20:
   
# #    if n < 10:

# #      print("too low")

# #    elif n > 20:

# #       print(" too high")

# #    n = int(input("try again: "))    

# # print("Thank you")


# # wap to find the perfect number   # 6 = 1+2+3

# n = int(input("Enter a number: "))

# temp = n

# div = 1

# sum = 0

# while div < n:
    
#     if n % div == 0:
        
#       sum += div

#     div += 1


# if sum == temp:

#    print(f"{temp} is a perfect number")

# else:

#    print(f"get out")            



# harshad number is an integer that is divisible by the sum of its digits
# ex: 9 + 9 = 18 and 18 is divisible by 9
        
# n = 18

# temp = n


# sum = 0

# while  n > 0:
    
#    div = n % 10

#    sum += div

#    n = n // 10

# if temp % sum == 0:

#    print(f"{temp} is harshad number")

# else:

#    print("get out")   


# most recursive (most repeated) character

# a = input("Enter a word: ")

# max = 0


# # for i in a:

# #     if a.count(i) > 0:


# #         max = a.count(i)

# #         element = i
# # print(f"element is {element} and count is {max}")


# #  wap to find the sum of first n number and n is entered by user

# # n = int(input("Enter the number: "))

# # sum = 0

# # for i in range(1,n+1):

# #     sum = sum + i

# # print(sum)    



# # wap to find the duplicate chracter or recursive character


# # name ="mohanlal"

# # for i in name:

# #     print(f"The name is {i} and {name.count(i)}")


# # wap to find a number is perfect number

# n = int(input("Enter a number: "))

# i = 1

# sum = 0

# for i in range(1,n):

#     if n % i == 0:

#      sum += i

# if sum == n:
#   print(f"{sum} is a perfect number")

# else:
#     print("get out")    

          
# ask the people "how many people you want to invite"  if number below 10 ask for the  "name and dispaly [name, has been invited"]
#  if above 10  "too many people".

# guest = int(input("Enter the number of people: "))

# if guest > 10:

#     print("Too many people")


# elif guest < 10:

#     for i in range(guest):

#         name = input("Enter the name: ")

#     print(f"{name}, has been invited")    



# wap to find the sum of digits in value entered by user.

# n ="yuegygd56674874878"

# sum = 0

# for i in n:

#     if i.isdigit():

#         sum += int(i)

# print(sum)        

# find the index of a target

# given  a string and a target value. use  for loop to find and display the index of the target value. if the target value is not 

# in the list. display a msg saying its not found.
# 

# name = input("Enter a word: ")

# value = input("Enter the target value: ")


# for i in range (len(name)):

#     if name[i] == value:

#         print(f"{value} of character is present at index {i}")

# # if name[i] != value:

# #         print(f"it is not found at {i}")    


# # name = input("Enter a word: ")

# # value = input("Enter the target value: ")


# # for i in range (len(name)):

# #     if name[i] == value:

# #         print(f"{value} of character is present at index {i}")

# # if name[i] != value:

# #         print(f"it is not found at {i}")    


# # Reverse a string

# # wap to reverse a string using for a loop

# # ex: python as nohtop  

# # text = "python"

# # rev = ""

# # i = 0

# # for i in range (len(text)):

# #     if i < (len(text)):

# #         rev = text[i] + rev

# #         i += 1

# # print(rev)    

# #  1. Count Vowels and Consonants

# # Write a program to count the number of vowels and consonants in a string.
# # Input: "hello world"
# # Output:
# # Vowels: 3
# # Consonants: 7

# text = "hello world"

# vowels = "aeiou"

# vowel_count = 0

# Consonant_count = 0

# for i in text:

#     if i in vowels:

#         vowel_count += 1



#     elif i.isalpha() and  i not in vowels:

#         Consonant_count += 1


# print(f"Vowel count is: {vowel_count}")

# print(f"Consonant count is: {Consonant_count}")

 #  wap to find the prime number.

# is a number tht is divided by itself and 1

# number = int(input("Enter a number: "))

# while number <= 1:

#     for i in range(2, number):

#         if number % i == 0:

#             print("It is not a prime number")

#         break
# else:

#         print("it is a prime number")

# break # is used to terminate the loop when given condition is met.

# i = 1

# while (i < 10):

#     print(i)

#     if i == 4:
#         break

#     i += 1

########### coontinue  which skips the condition is true 

# for i in range(1,5):

#     if i == 3:

#         continue

#     print(i)
  
# wap to print even numbers from the range 1,30

# for i in range(1,30):    # here if the condition  is true which skips 

#     if i % 2 != 0:

#         continue
#     print(i)

# wap to find the index and first occurence of the text

# text = input("Enter the text: ")

# target = input("Enter the text: ")

# for i in text:

#     if i == target:

#         print(text.index(i))

#         break
# else:
#         print(" not found")


# # prime or not

# number = int(input("Enter a number: "))

# while number < 1:
  
#     print("please enter a number greater than one:")

#     number = int(input("Enter a number: "))

#     for i in range(2,number):

#       if  number % i == 0:
      
#         print("it is not a prime")

#     break
# else:

#   print("it is a prime")    

# sum of digits

# wap to calculate sum of digits of a number provided by the user. use a for loop to iterate over the digits.

# Iterate over the digits" means going through each individual digit in a number one by one, usually using a loop.


# number = input("Enter the number: ")

# sum = 0

# for i in number:

#     sum = sum +  int(i)

# print(f"sum is: {sum}")

# Even numbers in range.
# wap to display all even numbers between two integers provided by the user.

# n1 = int(input("Enter a number: "))

# n2 = int(input("Enter a number: "))

# for i in range(n1,n2):

#     if i % 2 == 0:

#         print(i)

# find the index of a target

# given  a string and a target value. use  for loop to find and display the index of the target value. if the target value is not 

# in the list. display a msg saying its not found.


# text = "helloworld"

# target = "l"

# for i in text:

#     if i == target:

#         print(text.index(i))

#         break

#     else:

#      print("it is not found")        


# Reverse a string

# wap to reverse a string using for a loop

# # ex: python as nohtop

# text = "python"

# rev = ""

# i = 1

# for i in range (len(text)):

#     if i < len(text):

#         rev =  text[i] + rev 
    
#         i += 1  

#     print(rev)      



# # Given a string, count the frequency of each character using a for loop and display the results.


# # text ="helloworld"
      

# # count = 0

# # for i in range(len(text)):

# #     if i > count:

# #         count = count + i


# # print(count)     

# # wap to check palliandrome or not

# # text = "python"

# # rev = ""

# # i = 0

# # while (i < len(text)):

# #     rev = text[i] + rev

# #     i += 1

# # print (rev)


# # for i in range(len(text)):

# #     if i < len(text):

# #         rev = text[i] + rev

# # #         i += 1
# # # print(rev)        


# # # perfect number


# # n = int(input("Enter a number: "))

# # sum = 0

# # div = 1

# # while div < n:

# #     if n % div == 0:

# #       sum += div

# #       div += 1

# # print(sum)        

# text = "hellopython"

    
# for i in text:
    
#     if i == "p":
        
#         index = text.index(i)

#         element = text[0:index]

#         el = text[index::]

      

# print(element[::-1] + el[::-1])


# text = "hellopython"

# if "p" in text:  # Check if 'p' exists in the string
#     index = text.index("p")  # Find the index of 'p'
#     before_p = text[:index]  # Get the part before 'p'
#     after_p = text[index + 1:]  # Get the part after 'p'
#     result = before_p[::-1] + "p" + after_p[::-1]  # Reverse both parts and combine
#     print(result)
# else:
#     print("The letter 'p' is not in the string.")


# text = "hellopython"

# for i in text:
    
#     if i == "p":
        
#         index =text.index(i)

#         element = text[0:index]

# print(element[::-1] + text[index::])        


#prime range

# for j in range (1,10):
    
#     if j > 1:
        
#         for i in range (2,j):
            
#             if j % i == 0:
                
#                 print(f"{j} is not a prime number")
#                 break


#         else:  

#               print(f"{j} is a prime number") 
            
    
    
#     else:
#           print("prime number should be greater than one")     


# write a for loop that iterates from 1 to 100. 
# print "Fizz" for multiples of 3.
# print  "Buzz" for mutiples of 5 
# print "FizzBuzz" for multiples of both 3 and 5.

# n = int(input("Enter a number : "))
# for i in range(1,100):
    
#     if n % 3 == 0 and n % 5 != 0:
        
#         print("fizz")
#         break

#     elif n % 5 ==  0 and n % 3 != 0:
# #         print("Buzz")
# #         break  

# #     elif n % 5 == 0 and n % 3 == 0:
# #         print("FizzBuzz") 
# #         break   

# # harshad

# n = 156

# sum = 0

# for i in str(n):
    
#     sum = sum + int(i)

# print(sum)


# if sum % n == 0:
    
#     print("it is a harshad number")

# else:

#     print("it is not a harshad number")    



# sum of first n numbers

#  wap to find the sum of first n number and n is entered by user

# n = int(input("Enter a number: "))  

# sum = 0

# for i in range(1,n+1):
    
#     sum =sum + i

# print(sum)    

# wap to check a string is palliandrome.

# text = "madam"
# i = 0

# rev =""

# for i in text:
  
#      rev = text + rev
#      break


# print(rev)    
# ask the people "how many people you want to invite"  if number below 10 ask for the  "name and dispaly [name, has been invited"]
#  if above 10  "too many people"

# visitors = int(input("Enter the number: "))

# if visitors > 10:

#   print("Too many people")    

# elif visitors < 10:

#   for i in range(visitors):

#     name = input("Enter the name: ")

#     print(f"{name}, have been invited")            
# 
# wap to print  leap year                                 

# year = int(input("Enter a number: "))

# if (year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    
#     print(f"{year} is a leap year")

# else:
#     print(f"{year} is not a leap year")   
# 
# wap to print a number is armstrong or not
 
# n = 153

# temp = n

# length = len(str(n))

# sum = 0

# while n > 0:
    
#     digit = n % 10

#     sum += digit ** length

#     n = n // 10
# print(sum)    

# wap to check a number is palliandrome or not.

# # n = 121

# # temp = n

# # sum = 0

# # rev = 0

# # while n > 0:
    
# #     digit = n % 10

# #     rev = rev * 10 + digit

# #     n = n // 10

# # print(rev)    


# # Ask for the name of somebody the user wants to invite to a party. after this, dislay the message "[name]" has been now invited.

# #and add 1 to the count. Then ask if they want to invite somebody else .keep repeating this until they no longer want to invite anyone else to the party and 
# # then display how many people they have coming to the party..
# # count  = 0

# # guest = input("Enter the name: ")

# # print(f"{guest} has been now invited")

# # while True:
# #     option = input("Do you want invite somebody? (yes or no:)")

# #     if option == "yes":
        
# #         name = input("Enter the name:")

# #         count += 1


# #Armstrong

# # n = 153

# # sum = 0
# # length = len(str(n))

# # while n > 0:

# #     digit = n % 10

# #     sum += digit  ** length

# #     n = n // 10

# # print(sum)

# # palliandrome

# n = 121

# rev = 0

# temp = n

# while n > 0:

#     digit = n % 10

#     rev = rev * 10 + digit

#     n = n // 10

# print(rev)    

# if rev == temp:

#     print(f"{rev} is palliandrome")

# else:
#     print("it is not palliandrome")


        
#string palliandrome

# text = "madam"

# rev = ""

# for i in text:

#     rev = i + rev
# print(rev)    

#recursive index

text = "hellopython"

# for i in text:

#     if i == "p":

#      index = text.index(i)

#      element = text[0:index]

# print(element[::-1] + text[index::])     

# for i in text:

#     if i == "p":

#         index = text.index(i)

#         element  = text[index::]

#         print(text[0:index]+ ""+ element[::-1])


#         #  print(element[::-1] + text[index::])


# n = 156

# # sum = 0

# # for i in str(n):

# #     sum = sum + int(i)

# # print(sum)

# # if n % sum == 0:

# #     print(f"{n} is a harshad number")
# # else:
# #     print("it is a harshad number")  
# # 
# #   1. Count Vowels and Consonants

# # Write a program to count the number of vowels and consonants in a string.
# # Input: "hello world"
# # Output:
# # Vowels: 3
# # Consonants: 7
# # 

# text = "hello world"

# vowel_count = 0

# consonant_count = 0

# vowels = "aeiou"
# for i in text:

#     if i in vowels:
       
#        vowel_count += 1


#        print(f"The vowels are:{i}")

       
#     elif i not in vowels  and i.isalpha():
        
#         consonant_count +=  1


#         print(f"The consonants are: {i}")
# print(f"The vowel count is:{vowel_count}")

# print(f"The consonant count is: {consonant_count}")


# # prime number

# for j in range(1,10):

#     if j > 1:

#         for i in range (2,j):

#             if j % i == 0:

#                 print(f"{j} is not a prime number")
#                 break
#         else:
#              print(f"{j} is a prime number")

#     else:

#         print("prime number should be greater than one")         

# find the recursive character.

# text = "hello world"
# max = 0
# for i in text:
#     if text.count (i) > max:

#         max = text.count(i)
#         element = i
# print(f" element is{element} and count is {max}")      


# factorial

# def factorial(num):

#     fact = 1

#     for i in range(1, num + 1):

#         fact = fact * i

#     return fact
# num = int(input("Enter a number: "))

# print(f"The factorial of {num} is {(factorial(num))}")


# def sum(*args):

#     print(args)

#     sum = 0

#     for i in args:
#         sum += i

# #     print(f"sum is {sum}")    


# # sum(6,7,1)

# # sum(2,5,1)

# # wap to find the sum of odd n even numbers
# # using function


# def sum(*args):

#     odd_sum = 0

#     even_sum = 0

#     for i  in args:

#         if i % 2 != 0:

#             odd_sum += i

#         else:

#             even_sum += i  

#     print(f"sum of odd number is : {odd_sum}") 

#     print(f"sum of even number is :{even_sum}")   


# sum(4,7,2)

# sum(7,8,9)




# wap to find the factors of even numbers using function with parameters as args
def even(*args):

    for i in args:

        if i % 2 == 0:

            for j in range(1,i):

                if i % j == 0:

                 print(j) 

even(6,9,2)                            
