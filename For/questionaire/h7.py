

# 2. Find Palindromic Words

# Write a program to find and display all palindromic words in a given sentence.

# Example:
# Input: "madam'

text = input("Enter the text: ")

temp = text

rev = ""

for i in range(len(text)):
        
        if i < len(text):
       
         rev = rev + text[i]

         i += 1


print(rev)  

if rev == temp:
        
     print(f"{rev} is palliandrome")

else:

    print(f"{rev} is not palliandrome")        
