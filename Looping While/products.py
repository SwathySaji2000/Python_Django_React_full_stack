# wap to find the products of digits entered by user.



num = 156

i = 0

prod = 1

num = str(num)

while i < len(num):

    prod = prod * int(num[i])

    i = i + 1

print(prod)   




