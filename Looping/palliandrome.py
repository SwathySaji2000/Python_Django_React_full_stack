# wap to find a number is palliandrome or not

num = 121  

rev = 0

temp = num

while num > 0:

    digit = num % 10   # 121 % 10 = 1

    rev = rev * 10 + digit  # 0 * 10 + 1 = 1            

    num = num // 10  # floor division continues


print(rev)

if rev == temp:  # checking the reversed number === original number stored in temp

    print("It is a palliandrome number")

else:

    print("It is not a palliandrome number")

