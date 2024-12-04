# Ask the user's age . if they are 18 0r over , 
# display the message " you can vote", if they are aged 17, 
#             "  you can learn to drive" , if they are 16
# display the message " you can buy a lottery ticket"
# if they are under 16, dispaly the msg " you can go trick or treating "
# 


age = int(input("Enter your age: "))

if ( age >=  18):
     print("you can vote")

elif age == 17:

    print("you can learn to drive")     

elif age == 16:

     print(" you can buy a lottery ticket")    
else:
     
     print("you can go trick or treating")
