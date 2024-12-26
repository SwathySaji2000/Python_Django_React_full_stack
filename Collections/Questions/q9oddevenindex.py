
# wap to print sum of even and odd indexed digits in a given number


number = [4,5,7,8,2,1]

even_sum = 0

odd_sum = 0



for i in number:

    if number.index(i) % 2 == 0:

        even_sum = even_sum + i

    elif number.index(i) % 2 != 0:
         
         odd_sum = odd_sum + i    


print(f"sum of even numbers is :{even_sum}")

print(f" sum of odd numbers is: {odd_sum}")  


        
    
# for j in number:

#         if number.index(j) % 2 != 0:

#             odd_sum =odd_sum + j

# print(f" sum of odd numbers is: {odd_sum}")  

    



        


