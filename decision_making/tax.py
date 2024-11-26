#wap to calculate the taxof bike.

#cost of bike greater than 1 lakh >> tax = 15%

#cost of bike greater than 50k and less than or equal to 1 lakh >> tax = 10%

#cost of bike less than or equal to 50k >> tax =7%

#display the total price(cost + tax) to the customer


price = int(input("Enter the amount of bike: "))

if price > 100000:

    tax = (price * 15) / 100

    print(f"your total price is {tax + price}")

elif price > 50000 and  price <= 1000000:

    tax = (price * 10) / 100

    print(f"your total is {tax + price} ")

else:

    tax = (price * 7) /100

    print(f"your total price is{tax + price}")





#wap to calculate the taxof bike.

#cost of bike greater than 1 lakh >> tax = 15%

#cost of bike greater than 50k and less than or equal to 1 lakh >> tax = 10%

#cost of bike less than or equal to 50k >> tax =7%

#display the total price(cost + tax) to the customer



# price = int(input("Enter the amount of bike: "))

# if price > 100000:

#     tax = (price * 15) / 100

#     print(f"Total price is {price + tax}")

# elif price < 500000 and price <= 100000:

#     tax = (price * 10) / 100

#     print(f"your total price is {price + tax}")

# elif price  <= 50000:

#     tax = (price * 7) / 100

#     print(f"total price is {price + tax}!")     

    
