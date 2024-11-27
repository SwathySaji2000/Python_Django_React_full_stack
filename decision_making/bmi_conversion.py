# wap to calculate the bmi


#underweight: Less than 18.5
# normal weight: 18.5 to 24.9
#overweight : 25 to 29.9
#obese class 1: 30 to 34.9
#obese class 2: 35 to 39.9
#obese class 3: more than 40



weight_kg = float(input("Enter the weight (in kg) : "))

height_cm = float(input("Enter the height (in cm) : "))

height_m = height_cm / 100

bmi = weight_kg / (height_m ** 2)

if bmi < 18.5:

    print(f"{bmi} is under weight")

elif 18.5 <= bmi < 24.9:

    print(f"{bmi} is normal weight")    
 
elif  25 <= bmi < 29.9:
    print(f"{bmi} is overweight ")

elif 30 <= bmi < 34.9:

    print(f"{bmi} is obese class 1")

elif 35 <= bmi < 39.9:
    print(f"{bmi} is obese class 2")

else:
    print(f"{bmi} is obese class 3")    



# Input from the user
weight_kg = float(input("Enter the weight (in kg): "))
height_cm = float(input("Enter the height (in cm): "))

# Convert height to meters
height_m = height_cm / 100

# Calculate BMI
bmi = weight_kg / (height_m ** 2)

# Determine BMI category
if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f}. You are underweight.")
elif 18.5 <= bmi < 24.9:
    print(f"Your BMI is {bmi:.2f}. You have a normal weight.")
elif 25 <= bmi < 29.9:
    print(f"Your BMI is {bmi:.2f}. You are overweight.")
elif 30 <= bmi < 34.9:
    print(f"Your BMI is {bmi:.2f}. You are in obese class 1.")
elif 35 <= bmi < 39.9:
    print(f"Your BMI is {bmi:.2f}. You are in obese class 2.")
else:
    print(f"Your BMI is {bmi:.2f}. You are in obese class 3.")
