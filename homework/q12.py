
# Ask for two numbers, if the  first one is larger than the second, display the second number first and then the first number, 
# 
# otherwise show the first number first and then the second.

n1 = int(input("Enter a number: "))

n2 = int(input("Enter a number: "))

if n1 > n2:

    print(f"{n2}  and {n1}")

elif n2 > n1:

    print(f"{n1} and {n2}")    

