# wap to remove the first occurence of a given element in the list.

# element will be entered by user

number = [1,2,3,4,6,7,3,4]


n = int(input("Enter a number: "))


for i in number:

    if i == n:

     number.pop(number.index(i))  
     print(number)
     break


else:

   print("number is not in the list")  

   







