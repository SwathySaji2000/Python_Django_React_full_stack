# Ask the user to enter a number and then  enter another number. Add these two numbers together and then ask if they want 

# to add another number. if they enter "y", ask them to enter another number and keep adding numbers until they do not 

# answer "y". once the loop has started , display  the total.


total = 0

num1 = int(input("Enter a number: "))

total += num1

num2 = int(input("Enter a number: "))

total += num2

while  True:

    choice = input("Do you want to enter another number ? (yes or no):")

    if choice == "yes":  

        num = int(input("Enter another number: "))

        total += num

    else:
         
      break

print(f"The total is: {total}")




