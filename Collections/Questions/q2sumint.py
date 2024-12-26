
# Write a function  that takes a positive integer n and returns the sum of its digits.


def positive(n):
  
    sum = 0

    for i in str(n):
          
          if n < 0:
           
           print("Enter a positive integer:") 

          sum = sum + int(i)

            
    print(sum)  

positive(17)


