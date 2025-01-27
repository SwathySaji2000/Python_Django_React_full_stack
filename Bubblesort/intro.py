numbers = [5,4,3,2,6,8,10]

n = len(numbers) # 7

for i in range(n): # (0....6)  ist loop i =0

    for j in range(0,n-i-1): # (0-7-1)

        if numbers[j] > numbers[j+1]:  # number[0] > number[1]


            numbers[j],numbers[j+1] = numbers[j+1],numbers[j]


print(numbers)



