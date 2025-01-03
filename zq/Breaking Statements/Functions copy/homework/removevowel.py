# wap to remove the vowel from a string

# i/p ==> text == hello

# o/p ==> hll


def remove_vowel(*args):

    vo = "aeiouAEIOU"

    result = ""

    for  i in args:

        for j in i:

         if j not in vo:

            result += j

    return(result)

input_text = "hello"

output = remove_vowel(input_text)

print(f"output:{output}")

