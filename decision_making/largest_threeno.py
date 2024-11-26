#wap to find the largest among 3 numbers.


num1 = int(input("Enter the value: "))
num2 = int(input("Enter the value: "))
num3 = int(input("Enter the value: "))

# 0,0,-1

if num1 > num2 and num1 > num3:   # 0 > 0 and 0 >-1 false and true ==> false
    
    print(f"{num1} is greatest")


elif num2 > num1 and num2 > num3:   # 0 > -1 and 0 > 0  true and false ==> false

    print(f"{num2} is greatest") 


else:                        # -1 is greatest

    print(f"{num3} is greatest")



# elif num3 > num2 and num3 > num1:

#     print(f"{num3} is greatest")

