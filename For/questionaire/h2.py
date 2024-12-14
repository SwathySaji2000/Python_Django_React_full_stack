# Even numbers in range.
# wap to display all even numbers between two integers provided by the user.


start = int(input("Enter a number: "))

end = int(input("Enter a number: "))

print(f"The even numbers between {start} and {end} is:")

for i in range(start, end ):
        
        if i % 2 == 0:
         
         print(i)
                

                

