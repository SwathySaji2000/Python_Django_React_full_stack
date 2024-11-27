# wap to calculate the bmi


#underweight: Less than 18.5
# normal weight: 18.5 to 24.9
#overweight : 25 to 29.9
#obese class 1: 30 to 34.9
#obese class 2: 35 to 39.9
#obese class 3: more than 40



weight_kg = float(input("Enter the weight: "))

height_cm = float(input("Enter the height: "))

height_m = height_cm / 100

bmi = weight_kg / (height_cm ** 2)

if weight_kg < 18.5:

    print(f"{bmi} is under weight")

elif 18.5 <= weight_kg < 24.9:

    print(f"{bmi} is normal weight")    
 
elif  25 <= weight_kg < 29.9:
    print(f"{bmi} is overweight ")

elif 30 <= weight_kg < 34.9:

    print(f"{bmi} is obese class 1")

elif 35 <= weight_kg < 39.9:
    print(f"{bmi} is obese class 2")

else:
    print(f"{bmi} is obese class 3")    

