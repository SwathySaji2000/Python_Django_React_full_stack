
# find most recursive element from the text using dict


text = "ABBCCADEAA"

d_c = {}




for i in text:

    d_c[i] = text.count(i)

print(d_c)
      
      
max = 0

for key , value in d_c.items():

    if value > max:
        max = value
        element = key
print(max,element)        


    