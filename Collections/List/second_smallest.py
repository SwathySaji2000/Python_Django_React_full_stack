
# wap to find the second smallest from the list

numbers = [1,2,3,5,6]

smallest = numbers[0]

sec_smallest = numbers[1]

for i in numbers:

    if i < smallest:

        sec_smallest = smallest


        smallest = i

    elif i >  smallest and i < sec_smallest:

        sec_smallest = i

print(f" the second smallest is: {sec_smallest}")            