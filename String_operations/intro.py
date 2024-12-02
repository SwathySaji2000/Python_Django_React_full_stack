
############################## String Operations ##############################

#class str


name = "Luminar" # collection of characters

#string object

#string object_name[index]

#use of index
#========================
# {acessing specific elements in string or collection of characters}
#{searchimg element in string or collection of characters}
#{modifying elements in string ""}
#{it allows iterating}


# name = "Luminar"  # collection of characters
# print(name[1])  #o/p => u
# print (name[6])  #o/p => r
# #print (name[15]) # o/p => out of range.

# #======================================

# #wap to get the last element from  string  enter by user 
# name = input("Enter your name: ")

# # -1 negative indexing

# print(f"The last element is {(name[-1])}")


#================  slicing ===============================

text = "file handling in python"

# total count of characters
print(len(text))

# slicing a part   # counting includes spaces

print(text[0 : 4])  # [starting index : ending index]   upto ending index -1 slicing

print(text[9 : 16])  #  op ==> handling in python

print(text[4 :: ])  #  or  [:]  # starting with 4th position to last

print(text[:: -1])   # to rotate the string



#count()  no of times a specified values appears.

#endswith()  return true if the string ends with the specified value

#index() searches the string for a specified value and returns the position of where it was found.

#strip()   returns a trimmed version of the string  removes whitespaces


#join()  converts the element of an iterable into a string