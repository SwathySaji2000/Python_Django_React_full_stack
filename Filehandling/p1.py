   # create a new file "python.txt" and write " python is object oriented"

# read the content from python.txt and dispaly  and append " programming language"


file = open("python.txt","w")

file.write("python is object oriented")

file.close()



file = open("python.txt","r")

print(file.read())

file.close()

file = open("python.txt","a")

file.write(" programming language")

file.close()

file = open("python.txt","r")

print(file.read())