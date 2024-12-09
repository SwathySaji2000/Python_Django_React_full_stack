#  1. Count Vowels and Consonants

# Write a program to count the number of vowels and consonants in a string.
# Input: "hello world"
# Output:
# Vowels: 3
# Consonants: 7

text = "hello world"

vowels = "aeiou"

vowel_count = 0

consonant_count = 0

for i in text:

    if i in vowels:
     
     vowel_count += 1

     print(f"vowels: {i}")  


    elif i.isalpha() and i not in vowels:
       
       consonant_count += 1

       print(f"The consonants are: {i}")   

print(f"Vowel count is: {vowel_count}")

print(f"Consonant count is: {consonant_count} ")

