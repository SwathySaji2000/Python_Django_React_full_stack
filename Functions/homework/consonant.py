

#  wap to return true if all the consonant in a  string is unique



def consonant(*args):

    c = "bcdfghjklmnpqrstvwxyz"

    result = ""

    for i in args:

        for j in i:

            if j in c:      # and text.count != 1

                if j in result:     # return false
                 
                 return (False)         # break

            result += j                # return true

    return(True)

input = "python"        
output = consonant(input)
print(f"output is : {output}")    
