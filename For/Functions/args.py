

######                         args                                #####
   
###

# to pass a variable number of arguments to a function  ============>>>  args
 
def sum(*args):
   
    print(args)

    sum = 0

    for i in args:

        sum += i

    print(sum)
 

sum(1,2,3,4) 

sum(5,6)
sum(1)




# ==> iterable  if there is iterable use for we used to call the variable individually






