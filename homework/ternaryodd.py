# wap to check the number is even 0r odd using ternary

# n = int(input("Enter a number"))

# print(f"{n} is even "if n % 2 == 0 else f"{n} is odd" )


# wap to print "odd" if last digit of number enter by user is odd else even using  ternary

n = int(input("Enter a number: "))

res = n % 10

print(f"{res} is odd " if res % 2 != 0 else f"{res} is even")