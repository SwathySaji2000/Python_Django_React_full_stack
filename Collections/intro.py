 

#****** Collections *******

# a variable stores different tpes of values  or elements


# **** LIST* ****   is a collection of hetrogenous elements.

# * it is defined  by []  or List()

# hetrogenous collection

# allows duplicates  because of index

# maintains order  ""

#  method   ===>  object.append()  ,,, method used to add an element to the existing list or end of an list
            



#   string and list are linked because of index , 

#  List is iterable  


items = ["hello",1,1,2,7.6,True]

print(items[0])

print(items[0][4])

print(items[0:2])  ### slicing


items.append("swathy")

print(items)


##****************** pop remove and return items at last index
k = items.pop(2)  

print(k)

print(items)


#******************  insert (index and element)
items.insert(2,"geethy")
print(items)