#wap to identify the bar

#for men: BMR = 88.362 + (13.397 * weight in kg) + (4.799 * height in cm) - (5.677 * age in years)
#for women: BMR = 447.593 + (9.247 * weight in kg) + (3.098 * height in cm) - (4.330 * age in years)

weight_kg = int(input("Enter your weight :"))
height_cm = int(input("Enter your height :"))
age = int(input("Enter your age :"))
bmr = 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age)
print(f"The  BMR result is {bmr}")




