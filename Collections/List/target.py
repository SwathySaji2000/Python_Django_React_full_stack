

# given an array of integers num and an integer target,

#  return indices of the two numbers such that they add up to target.

numbers = [1,2,3,4]  

target = 7         

# index = []

# # indices = [2,3]

# for i in numbers:    # 1,2,3,4  then  i = 1 so ...on

#     for j in numbers:  # 1,2,3,4  then  i = 1  so ...on


#         if  i + j == target:                     

#             a = numbers.index(i)

#             b = numbers.index(j)

#             break


# index.append(a)

# index.append(b)

# print(index)

for i in range(len(numbers)):    # 0,1,2,3  based on length and index

    for j in range(len(numbers)):    # 1,2,3   

        if numbers[i] + numbers[j] == target:    #number[2] + number[3] = 7

            print(i,j)


            exit()      # is used to terminate ...
            