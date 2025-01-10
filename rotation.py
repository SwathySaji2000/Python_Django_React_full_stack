
# suppose an array of length n sorted  in ascending order is rotated between 1 and n times.

# ex the array numbers 

numbers = [1,2,3,4,5,6,7,8,9]
n  = int(input("Enter a number: "))

for i in range(n):
    numbers.insert(0,numbers.pop())

print(numbers)    



