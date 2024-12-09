# find the index of a target

# given  a string and a target value. use  for loop to find and display the index of the target value. if the target value is not 

# in the list. display a msg saying its not found.

name = "helloworld"

# value = input("Enter the target value: ")


# for i in range(len(name)):

#      if name[i] == value:
          
#         print(f"{value} is found at {i}")
   
#      elif name[i] != value:

#       print(f"{value} it is not found")      


target = "w"


for i in name:
    
   if i == target:
        
    print(name.index(i))

    break

   else:

    print("not found")

 
