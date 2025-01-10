
##########    Exception Handling  or Error Handling 


# """"""""""""""""""""
# They are usually caused by  invalid user input or code that is invalid in python.

# Exception Handling allows the prgm to continue to execute even if an error occurs.

#""""""""""""""""""""
# try

# except

# finally  ==> doesnt care about try n except execution of a program which produce the outcome


# if an exception occurs during execution of the try clause, the exception  may be handled by an except



a = int(input("Enter a number: "))

b = int(input("Enter a number: "))



try:

    result = a/b  
    
    print(result) 

except:

    print(" divide by zero is not possible")    
   
finally:
    print("thankyou")



