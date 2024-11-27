
# wap to take a student  mark as input and print their grade:
#  A for marks >= 90
#  B for marks 80 - 89
#  c for marks 70 - 79
#  F for marks < 70


mark = int(input("Enter the mark: "))

if mark >= 90:

    print(f" your grade is  : A")

elif  80 <=  mark <= 89: 

    print(f"your result is: B")    

elif  70 <= mark <= 79:

    print(f"your result is: C")    

else:

    print(f"your result is : F")
