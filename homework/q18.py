# ask the user to enter a number. it is under 10, dispaly the message 
# " too low". if their number is between 10 and 20 dispaly
# correct. otherwise dispaly "too high

num = int(input("Enter a number:"))

if num < 10:

    print("Too low")

elif (num > 10) and (num < 20):

    print("Correct")

else:

    print("Too high")