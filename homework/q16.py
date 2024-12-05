#  Ask the user if it is raining and convert their answer to lower case so it doesn't matter what case they type it in.
#  if they  answer "yes" , ask if it is windy. if  they answer "yes" to this second question, 
#  display the answer " it is too windy for an umbrella" , otherwise display the message . " take an umbrella ", otherwise
# display the message " Take an umbrella" . if they did not answer "yes" to the first question, display the answer "Enjoy your day"




w = input("if it is raining ?(yes or no):")




if w == "yes": 
    
    s = input("if it is windy?(yes or no):")

    
    if s == "yes":

     print("it is too windy for an umbrella")  

    else:

     print("Take an umbrella")


else:

    print("Enjoy your day")    


    











  



