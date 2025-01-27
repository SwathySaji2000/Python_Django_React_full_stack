


####### BLIND 75




# # You are given an array prices where prices[i] is the price of a given stock on the ith day.

# # You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# # Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# # Example 1:

# # Input: prices = [7,1,5,3,6,4]
# # Output: 5
# # Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# # Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# # Example 2:

# # Input: prices = [7,6,4,3,1]


# prices = [1,5,6,7,10]


# max_profit = 0

# for i in range(len(prices)): # 0

#     for j in range(i+1,len(prices)):  # 1 

#         if prices[j] - prices[i] > max_profit: 

# #             max_profit = prices[j] - prices[i]

# #             elements = [prices[i],prices[j]]

# # print(f"The max_profit is {max_profit} and the elements is {elements}")   





# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.



# # #find the sum of a list based on a target value == 8

# # numbers = [3,4,5,6,2]

# # result = 8

# # for i in range(len(numbers)):

# #     for j in range(i+1,len(numbers)):

# #         if numbers [i] + numbers[j] == result:

# #             print(f"elements are {numbers[i]} and {numbers [j]}, indexes are {i} and numbers{j}")


# num = [3,4,5,1,2]


# numbers = int(input("Enter the number: "))

# if numbers in num:

#     index = num.index(numbers)
#     print(index)


# for i in range(numbers):

#     num.insert(0,num.pop())


# print(num)     

#based on rotation pop the number based on index


### 333


s = " A man, a plan , a canal: Panama"

a = " "

for i in s:

    if i.isalnum == True:

        a = a + i

a = a.lower()

if a == a[::-1]:

  print("it is a palliandrome")























