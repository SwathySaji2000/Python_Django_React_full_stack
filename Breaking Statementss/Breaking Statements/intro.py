

#################################### Breaking statement ################################ include break, continue and pass.   
                        #  alter the loop so we use breaking statement
   



 #######################  BREAK #########################

#   use : performance side, time complexity and memmory management

# break is used to terminate  the loop when the given condition is met.   or alter
#  it is immediately used to stop the iterations.

# based on a condition ,, we can use jumping statement like break.

i = 1

while (i < 10):

    print(i)

    if i == 4:  # based on a condition we need to stop the iteration.

        break  

    i += 1




    #####################   CONTINUE #############

    # to execute the next iteration of the loop while skipping the current one

      # which skips the condition is true and loop continue


for i in range (1,5):

    if i == 3:      #  3 == 3 is true and which skips and loop continues

        continue

    print(i)      

# wap to print the even numbers from 1 to 30

for i in range(1,30):

    if i % 2 != 0:

        continue

    print(i)
