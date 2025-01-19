#write a function to check whether the string is pangram.

# "The quick  brown for jumps over the lazy dog" => sentence contain all letters

# from A to Z so its a pangram.


def pangram(text):

    
    letters = "abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXYZ"  # caps

    letters = letters.lower()


    

    for i in letters:

        if i not in text.lower():

            print("it is not a pangram")
            break

        else:

           print("it is a pangram")
           break


word = input("Enter the string: ")

pangram(word)

