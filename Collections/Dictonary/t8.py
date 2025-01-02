

# wap to concatenate using dict 


items = ["name","swathy","place","kottayam"]

element = {}
for i in range(len(items)):

    if i % 2 == 0:

        element[items[i]] = items[i+1]
print(element)        



