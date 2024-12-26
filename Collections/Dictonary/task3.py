items = "hello hai hello hai hi"
# {'hello': 2, 'hai': 2, 'hi': 1}

n = items.split()

# print(n)

d = {}


for i in n: 

    d[i] = n.count(i)


print(d)    

