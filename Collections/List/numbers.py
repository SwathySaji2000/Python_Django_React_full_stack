

#  read numbers from the user until user enters a value 0
#  then display the list of numbrs in ascending order
# 

num = int(input("Enter a number: "))

number = []

while(num != 0):

    number.append(num)

    num = int(input("Enter a number: "))

    print("number added")

    number.sort()

print(number)






    








