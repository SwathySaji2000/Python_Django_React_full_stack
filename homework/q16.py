#  Ask the user if it is raining and convert their answer to lower case so it doesn't matter what case they type it in.
#  if they  answer "yes" , ask if it is windy. if  they answer "yes" to this second question, 
#  display the answer " it is too windy for an umbrella" , otherwise display the message . " take an umbrella ", otherwise
# display the message " Take an umbrella" . if they did not answer "yes" to the first question, display the answer "Enjoy your day"


q = input(" Enter the climate condition:")

w = input("it is windy")

print(q.lower())

if q == True:
    
    print(w)

    
    if w == True:

     print("it is too windy for an umbrella")  

    elif w == False:

     print("Take an umbrella")


else:

    print("Enjoy your day")    


    
# # Ask if it is raining
# q = input("Is it raining? (yes or no): ").strip().lower()

# if q == "yes":
#     # Ask if it is windy
#     w = input("Is it windy? (yes or no): ").strip().lower()

#     if w == "yes":
#         print("It is too windy for an umbrella.")
#     else:
#         print("Take an umbrella.")
# else:
#     print("Enjoy your day!")










  



