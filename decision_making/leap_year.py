# wap  to find the year is leap year

year = int(input("Enter the year: "))

# checking the non- century , leap year) and checking the century , leap year 

# non century is not divisible by 100 , leap year is divisible by 4.    <<<<<<<<<<<==============>>>>>   non century.

# century is divisible by 100 and leap year is divisible by 400.

if (year % 100 != 0 and year % 4 == 0) or (year % 100 == 0 and year % 400 == 0):
       

    print(f"{year} is a leap year")

else:

    print(f"{year} is not a leap year")







