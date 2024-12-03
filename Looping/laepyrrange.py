# wap to print the numbers from 


start_limit = 1900

end_limit = 2024

i = 1900

while i <= end_limit:

    if ( i % 4 == 0 and i % 100 != 0) or (i % 100 == 0 and i % 400 == 0):

     
      print(i)


    i += 1    