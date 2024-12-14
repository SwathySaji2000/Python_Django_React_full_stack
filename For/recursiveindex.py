#text = "hellopython" o/p as ollhepython   

text = "hellopython"


if "p" not in text:
     
     print(text[::-1])


else:     

  for i in text:

     if i == "p":

         index = text.index(i)

         element = text[0:index]

print(element[::-1] + text[index::]) 


    # rev + concat

# for i in text:

#    if i == "p":

#       index = text.index(i)

# element = text[index::]

# print(text[0:index] + " " +  element[::-1])
    