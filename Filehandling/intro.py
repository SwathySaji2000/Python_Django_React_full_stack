

#  file handling


# file handling in python involoves operation such as

#  creating, reading, writing and closing files, utilizing various mode to manage  data..

# modes

# read "r"
# write "w"   if an existing file write() performs over write otherwise opens a new file
# append "a"




# syntax : open("filename","mode")

# open is a function


file= open("new.txt","r")

print(file.read())

#########################    write() creates a new file 

file = open("abc.txt","w")

file.write("hello python")


#############   


file = open("C:/Users/swath/OneDrive/Desktop/fullstack/Decision_Making/sample.txt","w")

file.write("Hello  World ")


################## append


file = open("abc.txt","a")
file.write(" django")


file = open("sample.txt","a")
file.write(" hi beautiful")












# wap to find the even number from list 

number = [1,2,4,5,6,8]



