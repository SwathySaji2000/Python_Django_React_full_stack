
text = "ABBCCDAE"

# wap to find using dict


dc ={}

for i in text:

    dc[i] = text.count(i)

print(dc)
    
for key,values in dc.items():

    if values == 1:
        print(key)    


# to print first recursive element

w_c = {}

for i in text: # A

    if i in w_c:  

        print(f"The first recursive element is: {i}")
        break

    else:
        w_c [i] = 1  
         # creating an empty dict to statisfy the condition  for the first loop dict stores A,B no recursive element then stores B 

