# wap to check a string is palliandrome

text = "qwerty"

rev = ""

i = 0

while (i < len(text)):  # text length nokum i <5

    rev = text[i] + rev  # rev = q + ""  ,,, rev = w + q,,,,,rev = 


    i += 1

print(rev)

if rev == text:

    print("it is palliandrome")

else:

    print("get out")    

