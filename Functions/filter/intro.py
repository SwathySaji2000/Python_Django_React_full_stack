

###################  FILTER  

# which shows the selected true answers 

# syntax : (function, argument: collection)


# wap to find hte number is divisible by 5 


numbers = [1,3,2,5,10,25]

result = list(filter(lambda a: a % 5 == 0,numbers))

print(result) 


result = list(filter(lambda a: a % 2 == 0,numbers))

print(result)