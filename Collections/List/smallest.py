
# wap to print the samallest number using function
def smallest(numbers):
   
   small = numbers[0]    # taking the first index of list.  except 0

   for i in numbers:
      
      if i < small:
         
         small = i

         return(small)
      
      
print(smallest([3,5,1,2,6])) 