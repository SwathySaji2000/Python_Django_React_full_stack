

#   create a new file and write " python is a programming language practise it"


# read the words from above which starts with letter "p" and display in a list


file = open("python.txt","w")

file.write("python is a programming language practise it")

file.close()

result = [ ]  # create a list for storing the letter starts with p

file = open("python.txt","r")

#print(file.read())   # python is a programming language practise it

#print(file.read().split( " "))  # ['python', 'is', 'a', 'programming', 'language', 'practise', 'it']

for i in file.read().split(" "):

    if "p" in i and i.index("p") == 0:    # because of spliting  each word starts with 0

        result.append(i)

print(result)    
