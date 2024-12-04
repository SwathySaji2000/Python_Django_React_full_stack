

# create a variable called number and set the value to 50. ask the user to enter a number while their guess is not the same as the
# compnum value, tell them if their guess is too low or too high and ask them to have another guess.
# if they enter the same value as compnum display the message "well done, you took [count] attempts".


number = 50

result = 0

count = 0


while result != number:   

    result = int(input("Enter a number: "))

    count += 1

    if result > number:

      print("too high")

    elif result < number:

      print("too low")

print(f"well done {count} attempts") 