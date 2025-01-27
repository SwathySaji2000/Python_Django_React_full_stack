# # Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer .
# #  Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, . 
# # Please use list comprehensions rather than multiple loops, as a learning exercise.
# # Print an array of the elements that do not sum to 3

# x = int(input("Enter a number:"))
# y = int(input("Enter a number:"))
# z= int(input("Enter a number:"))
# n = int(input("Enter a number:"))

# result = [[i,j,k]
#         for i in range(x + 1)

#         for j in range(y + 1)

# #         for k in range(z + 1)
# #         if i + j + k != n]

# # print(result)

# # Given the participants' score sheet for your University Sports Day, 
# # you are required to find the runner-up score. You are given  scores.
# # Store them in a list and find the second  score of the runner-up.



# def score(*args):
    
#     max_value = max(*args)
#     second_largest = None

#     for i in args:

#         if i != max_value and (second_largest is None  or i > second_largest):
            
#             second_largest = i

#     if second_largest is not None:
#             print(second_largest)

#     else:

#             print("No second largest found")    
                
        
# score([3,4,5,6])
        


# will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
# Print the average of the marks array for the student name provided, showing 2 places after the decimal.



# def average(*marks,student_name):
    

#     if(len(marks)) == 0:
#         return "No numbers provided"
    
    
#     sum = 0

    

# total =sum(marks)


# avg = sum / len(marks)


# student_details = {student_name: avg}

#   return student_details

# result = average("ammu",34,56,78)

# print("Average:", result)
    










