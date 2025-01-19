
#******************************** Reduce

#   bulit-in function that applies a  given function to the elements of an list reducing them to a single value.

# we can import reduce from functools


from functools import reduce

numbers = [1,2,3,4,5]

result =  reduce(lambda a,b: a+b,numbers)   # a=1,b=2, then a stores sum and b stores the variable and so on


print(result)

