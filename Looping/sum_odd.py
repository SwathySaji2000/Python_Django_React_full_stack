

# wap to print sum of odd numbers from a range 


start = int(input("Enter a value: "))

end = int(input("Enter a value: "))


sum = 0


while ( start <= end):

    if start % 2 != 0 :

        sum = sum + start

    start = start + 1   # i = i + 1

print(sum)    
    