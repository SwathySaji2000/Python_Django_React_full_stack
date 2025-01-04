

# map function
 
# syntx : (function,argument: expression,collection)


# The map() function is used to apply a given function to every item of an iterable,



# wap to find the number is divisible by 5

numbers =[ 1,3,5,9,15,20]

result = list(map(lambda a : a if a%5 == 0 else None,numbers))   # we use None in else part otherwise we need to   

# map(function,iterable)  # map applies to list or tuple in a function

print(result)