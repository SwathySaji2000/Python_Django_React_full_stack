

# wap to filter the mobiles with black in colour

mobiles={"Apple":{"model":"iphone15","price":120000,"color":"Black"},
         "Samsung":{"model":"S23 Ultra","price":180000,"color":"white"},
         "Sony":{"model":"xperia ultra","price":130000,"color":"red"},
         "Huawei":{"model":"Pura 70 ultra","price":170000,"color":"Black"}}


# for i in mobiles:

#     if mobiles[i]["color"] == "Black":

#         print(f"black color mobiles are : {i}")


#wap to filter te mobiles in price less than 150000

# for i in mobiles:

#   if mobiles[i]["price"] <= 150000:

#     print(i)
         

 # wap to filter mobile in range of 140000 to 200000

# for i in mobiles:
       
#        if mobiles[i]["price"] > 140000 and mobiles[i]["price"] < 200000:
          
#          print(i, mobiles[i]["model"])
   

# to update the price of sony

for i in mobiles:

    if i == "Sony":

        mobiles[i]["price"] = 1500000

print(mobiles)        



