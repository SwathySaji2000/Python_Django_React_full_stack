

#**************************************************** TUPLE ***********************

# Tuple is immutable which can't be modified


# it is  defined by () 

# tuple is iterable we cant modify.

# duplicates allowed.

# order maintains.

# insert and remove methods can't be used because it is not modified

# methods *****************************

# count and index

# items = (1,3.7,"hello",True,False)

# print(type(items))

# print(items.count(1))

# print(items.index("hello"))

# if a variable contain only one element we use " ," to identify class tuple  ex:a = ("hello ,") otherwise the interpreter reads the class as string


items = (1,3.7,"hello",True,False)

# wap to remove the last item of tuple  

items = list(items)  # converting to list

items.pop()

print(tuple(items))