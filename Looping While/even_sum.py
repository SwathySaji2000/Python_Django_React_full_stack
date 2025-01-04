# wap to print the sum of even number from a and b where a and b entered by user.

a = int(input("Enter a value: "))

b = int(input("Enter a value: "))

sum = 0

while a < b:
    
    if a % 2 == 0:
     
     sum = sum + a

    a = a + 1

print(sum)     