
# ask the user to enter a number. keep asking until they  enter a value over 5 and they display the message" The last number you entered was a 
# [number] and "stop the program. "

num = int(input("Enter a number: "))

while num <= 5:

    print(f"the  number is {num}")

    num = int(input("Enter a number: "))


print(f"The last entered number was {num}")        
