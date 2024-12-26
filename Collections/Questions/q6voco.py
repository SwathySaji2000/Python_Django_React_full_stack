# create a function to check  entered character is vowel or consonants


def character(text):


    vowels = "a,e,i,o,u"

    for i in str(text):

        if i in vowels:

            print(f"{i} is a vowel")

        else:

            print(f"{i} is a consonant")    

character("hello")