# sum of digits

# wap to calculate sum of digits of a number provided by the user. use a for loop to iterate over the digits.

# Iterate over the digits" means going through each individual digit in a number one by one, usually using a loop.

 # Python, iterable objects are those that can be looped over, such as strings, lists, tuples, and dictionaries.
  # an integer is a single value, so you cannot directly loop over it.

n = int(input("Enter the number: "))

sum = 0


for i in n:

    sum += i

print(f"The sum is: {sum}")   


