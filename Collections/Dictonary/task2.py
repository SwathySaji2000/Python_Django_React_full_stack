#N and we have to generate a dictonary that containsnumbers and their squares(i, i*i) using python

#N=int(input())

n =int(input("Enter the number: "))

items = {}

for  i in range(1,n+1):

    items[i] = i**2

print(items)    