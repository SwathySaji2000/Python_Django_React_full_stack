# most recursive (most repeated) character

name = "helloworld"

max = 0

for i in name:

    if name.count(i) > max:
          
      max = name.count(i)

      element = i

print(f"element = {element} and  count = {max}")     