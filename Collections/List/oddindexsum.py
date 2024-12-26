 

# wap to find the sum of numbers in the odd index position          

                             # odd inte index based sum anu

numbers = [1,4,7,5,4,3,9,10]

sum = 0

for i in numbers:

    if numbers.index(i) % 2 != 0:       

        sum += i

print(sum)        