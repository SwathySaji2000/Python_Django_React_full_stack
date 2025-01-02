items = {"a":[1,4,6],
         "b": [1,3,4],
         "c":[1,6,7]}


d = {}

print(items.items())

for k,v in items.items():  # k = a , v= [1,4,6]....

    for  i in v:

        if i > 5:

            break

    else:

        d[k] = v  # adding to dictonary to the value of v

print(d)        

 