# create a list from the specified start to end index of another list

numbers = [1,2,3,4,54,6,67,87]

# start_index = 3 , end_index = 5     0/p = [4,54,6]


start = int(input("Enter the start index: "))

end = int(input("Enter the end index: "))



element = []

for i in range(start,end+1):

    element.append(numbers[i])

print(element)