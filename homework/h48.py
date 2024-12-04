
# Ask for the name of somebody the user wants to invite to a party. after this, dislay the message "[name]" has been now invited.

#and add 1 to the count. Then ask if they want to invite somebody else .keep repeating this until they no longer want to invite anyone else to the party and 
# then display how many people they have coming to the party..

count = 0

guest1 = input("Enter the name: ")

print(f" {guest1} has been now invited")

count += 1

while True:

    option = input("Do you want to invite sombebody else ? (yes or no):")

    if option == "yes":

        guest = str(input("Enter the name: "))

        count += 1

    else:

        break

print(f"Total guests arrived in the party: {count}")        



        