

items = ["hello","python","hello","django"]

# create a file and write this list to it

# read the file and display the unique elements


file = open("p3.txt","w")

for i in items:

    file.write(i + "\n")

file.close()

list = [] 


file = open("p3.txt")


for i in file.readlines():    

    list.append(i.strip("\n"))  # remove \n 

print([ i  for i in list if list.count(i) == 1])    # list comprehension




