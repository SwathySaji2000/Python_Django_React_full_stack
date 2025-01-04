# wap to find the sum of digits enter by user


# num = 5678


# i =0
 
# sum = 0

# num = str(num)   # we are converting int to str we need to take index ,, so adding the digits by index

# while (i < len(num)):   #  index - length i e len = 3

#     sum = sum + int(num[i])  

#     i = i + 1

# print(sum)


num = int(input("Enter a number: "))

i = 0

sum = 0   # store cheyyan variable eduthu then oro loop anusarich sum inte values replace akum

num = str(num)   # converting int to string type then only find index of num


while(i < len(num)):  # based on length we set a value length - index

    sum = sum + int(num[i])   #  oro index sum cheyyunu

    i = i + 1   # increment value of i

print(sum)    



