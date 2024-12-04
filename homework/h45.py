
  

# set the total to 0 to start with. while the total is 50 or less, ask the user to input a number. 
# Add that number to  the total and print the message " The total is.. [total]"
# stop the loop when the total is over 50.


total = 0

while (total <= 50):    # kodukunna input less than 50 anenkil input chodichond erikum and athinte ellam total above 50 anenkil loop out varum and                         # total print akum

    num = int(input("Enter a number: "))   # 10 , 20 , 30 ,1  # total 51 

    total += num

print(f"The total is {total}")    
