

# wap to print the odd numbers from the list

# numbers = [1,2,3,4,5,4,3,2,7,8]

# odd_number = []


# for i in numbers:

#     if i % 2 != 0:

#         odd_number.append(i)

# print(odd_number)        


# numbers = [1,2,3,4,5,4,3,2,7,8]


numbers = [1,2,3,4,5,4,3,2,7,8]

odd_number = []

even_number = []

for i in numbers:

    if i % 2 != 0:

        odd_number.append(i)

        print(odd_number)

    

    elif i % 2 == 0:

        even_number.append(i)    

    print(even_number)    