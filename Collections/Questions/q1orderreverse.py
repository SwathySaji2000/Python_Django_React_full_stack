# Write a function  that reverses the order of words in a given sentence but keeps the characters in each word in the correct order.
# Example: "Hello World" → "World Hello"


def reverse (text):

    words = text.split()


    rev = ""

    for i in  reversed(words):   
      
      rev = rev + i + " "

    print(rev)  

reverse("Hello World")      

 # reversed() function takes the words list and returns an iterator 
       # that yields the elements of the list in reverse order

