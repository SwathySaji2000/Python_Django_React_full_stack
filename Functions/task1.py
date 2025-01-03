# given an string, return true if any value appears at least twice in the string.

# and return false if every element is distinct. using function.

def duplicate(text):

    for i in text:

        if text.count(i) > 1:

            return(True)
        
    else:

        return(False)   



print(duplicate(text ="mariya"))