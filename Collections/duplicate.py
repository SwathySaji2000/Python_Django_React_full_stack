

#  define a function which should return true if list contains atleast one duplicate element

#else return false


# numbers = [1,2,3,4,2,3,5,7]

def duplicates(numbers):
    for i in numbers:

      if numbers.count(i) > 1:

        return(True)
      
        break
      
      else:

        return(False)
      
print(duplicates([1,2,3,4,2,3,5,7]))      
    
