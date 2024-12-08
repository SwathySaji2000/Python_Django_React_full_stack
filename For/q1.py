# ask the people "how many people you want to invite"  if number below 10 ask for the  "name and dispaly [name, has been invited"]
#  if above 10  "too many people"


visitors = int(input("Enter the number of visitors: "))

if visitors > 10:

    print("Too many people")


elif visitors < 10:

    for i in range(visitors):

        name = input("Enter the name: ")

        print(f"{name} ,has been invited")




