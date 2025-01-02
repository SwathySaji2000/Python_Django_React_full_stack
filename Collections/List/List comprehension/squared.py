# wap to list of squared numbers from range 1 to n. where n is entered by user


n = int(input("Enter a number: "))

new = [ i ** 2 for i in range(1,n+1)]

print(new)


#  dictonary comprehension

d={i:i**2 for i in range(1,n+1)}

print(d)


# normal

# n = int(input)

# d = {}

# for i in range(1,n+1):

# d[i] = i**2