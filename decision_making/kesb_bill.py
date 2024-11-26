# less than 100 units >>>  5rs per unit

# 100 units >>> 7rs per unit

#greater than 100 >> 10 rs per unit

unit = int(input("Enter the unit: "))

if (unit < 100):

     
    print(f"The total bill is {unit * 5}")


elif (unit == 100):

    print(f"The total bill is {unit * 7}")


else:

    print(f"The total bill is {unit * 10}")    

# elif unit >= 100:

#  print(f"The total bill is {unit * 10}")


