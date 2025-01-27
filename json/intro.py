############ json == javascript object notation


# which is light weight

# easily understandable

# json uses small letters for boolean values

# In json key value will be string i.e int,bool

# json uses null value instead of None  , and we dont use " " for null



import json

data ='{"name":"swathy","age":null,"is_working":true}'  
# data1 ='{"name":"swathy","age":None,"is_working":True}'  

new  = json.loads(data)

print(new)

# s = json.loads(data1)



# print(s)