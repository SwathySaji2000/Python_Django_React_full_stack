# wap to print vowel

def vowel(*args):

    v = "aeiouAEIOU"

    result = ""

    for i in args:

        for j in i:

            if j in v:

                result += j

        return(result)        


input = ("hello")
output = vowel(input)

print(f"output :{output}")

