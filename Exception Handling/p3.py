

numbers = [1,23,45,89,90]

try: 
  print(numbers.index(int(input("Enter a number:"))))

except NameError:
  print("please enter a valid digit") 

except ValueError:

  print("please enter a valid value")  
