 
numbers = [1,2,3,4,5,6]


#  o/p  ==numbers = [4,5,6,1,2,3]   

for i in range(3):
  

  k = numbers.pop()  # uses default 


  numbers.insert(0,k)   #  insert(index, element)

print(numbers)