
# wap to print sum of elements in odd index

num = 145637  # 4 + 6 + 7

i = 0

sum = 0

num  = str(num)

while i < len(str(num)):

    if i % 2 != 0:

        sum = sum + int(num[i])   

    i = i + 1

print(sum)


