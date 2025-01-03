# Given a string, return a string for every character in the orginal there are three characters.

# hello == hhheeellllllooo

def string(text):
     
    new = "" 
    for i in text:

        new += i*3
    print(new)


word = input("Enter the string: ")
string(word)        