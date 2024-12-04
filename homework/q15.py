# Ask the user to enter the favourite color. if they enter "red" , "RED" or "Red" display the message "I liked too " , 
# otherwise  display the message " i dont like [color] , i prefer red".


color = input("Enter your favourite color: ")

if (color == "red") or (color =="RED") or (color == "Red"):

    print("I liked too")

else:

    print(f" i dont like {color} , i prefer red")    