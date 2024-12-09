
# . Character Frequency

# Write a program to count the frequency of each character in a string.



text = input("Enter the text: ")    # using 2 for loops and intialising char and i

counted = ""


for char in text:

    if char not in counted:   #Only process the character if it hasn't been counted yet

        count = 0

        
        # Loop through the string to count occurrences of the character

        for  i in text:

          if i == char:

            count += 1

            # Print the frequency of the character

        print(f"{char}:{count}")   

         # Mark the character as counted

        counted += char    





