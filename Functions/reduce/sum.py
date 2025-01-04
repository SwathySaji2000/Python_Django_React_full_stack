
#  filter all even numbers to a list

# find the product of them using reduce

number =[1,2,3,4,5,6,8,1]

result = list(filter(lambda a:a if a%2 == 0 else None,number))

print(result)

from functools import reduce

items = reduce(lambda a,b: a*b,result )

print(items)

items = reduce(lambda r: r**2,items)
