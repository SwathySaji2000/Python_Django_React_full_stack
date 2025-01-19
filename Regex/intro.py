


import re



##### Regular expression  ===== " based on  pattern"

#  is a special sequence of characters that uses a search pattern to find a string or set of strings.


# re.finditer()
# match()
# findall()



#######    Special Sequences 

#  \A = to check a string start with specified character

#  \d = to  check whether the string contain any digits

# \D = to check whether the string does not contain any digits

# . = a.c >>> any character in between a and c.

# * = >> zero or more occurences   [2md chara more occurencess]




# to find the pattern 

text = "helloworld"

pattern = "owo"


matcher = re.finditer(pattern,text) 
 # re is module ,which calls  functions {finditer }   # pattern has start(),end(),group() methods  

for i in matcher:

    print(f"starts with {i.start()}, ends with {i.end()},pattern is {i.group()}")


# text = "malayalam"

# pattern = "alay"

# matcher = re.finditer(pattern,text)

# for i in matcher:

#     print(f"starts with { i.start()}, ends with {i.end()}, pattern is {i.group()}")


text = "pachepache"

pattern = "ache"


matcher = re.finditer(pattern,text)

for i in matcher:
    print(f"start with {i.start()}, ends with {i.end()},patteren is {i.group()}")
 



