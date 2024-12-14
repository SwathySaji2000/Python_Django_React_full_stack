# for j in range(1,10):

#     if j > 1:

#         for i in range(2,j):

#             if j % i == 0:

#              print(f"{j} is not a prime number")
#              break

#         else:

#             print(f"{j} is a prime number")
          

#     else:
#         print("prime should be greater than one")    


text = "python"

# target = "o"

# for i in text:
#     if i == "o":

#         print(text.index(i))
# #         break
# #     else:
# #      print("not found")        
# rev = ""

# i = 0

# for i in  range (len(text)):

#     if (i < len(text)):
#         rev = text[i] + rev
# print(rev)        


#perfect number

# n = 6 
# i = 1

# sum = 0

# for i in range(1,n):

#     if n % i == 0:

#         sum += i

# print(sum)

# if n == sum:
#     print(f"{n} is perfect number")
# else:
#     print("get out")        

text = "helloworld"

dup = ""

for i in text:
    if i not in dup:
        dup += i
print(dup)        
