
# wap to check the number of digits in the number entered by user

value = "qwrty56673nhjhj90877"

for i in value:

    if i.isdigit():

        print(i)


# isdigit() method is used to check the values in digit or alpha


# wap to find the sum of digits in value entered by user.

value = "qwe34ujip789"

sum = 0

for i in value:

    if i.isdigit():

        sum += int(i)

print(sum)    