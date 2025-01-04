

## wap to find the vowels in a string entered by user using functions.

# abc The no of vowels in abc is 1


def vowels(*args):

    for i in args:  # i "abc"  "hello " collection of characters  >>>> no of vowels
         
        count = 0

        for j in i: # for j in "abc" , for j in "hello"

            if j in "aeiou":    # x in "aeiou"

                count += 1

        print(f"The number of vowels in {i} is {count}")        


vowels("abc","hello","wonderla")





