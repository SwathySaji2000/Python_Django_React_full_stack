#days = 7

# day = int(input("Number of days:"))
# hours = int(input("Number of hours:"))
# minutes = int(input("Number of minutes:"))
# seconds = int(input("Number of seconds: "))

# t_hours = day * 24
# t_minutes = hours * 60
# t_seconds = minutes * 60

# print(f"{t_hours} in hours, {t_minutes} in minutes, {t_seconds} in seconds")



#Task the user to enter a number over 100 and then enter a number under 10 and tell how many times the smaller number goes into the larger number in a user friendly manner

larger_num = float(input("Enter a larger number: "))
smaller_num = int(input("Enter a smaller number: "))

print(f"The smaller number goes into the larger number is {larger_num // smaller_num}")