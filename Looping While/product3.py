# wap to find the product of numbers divisible by 3 from 1 to 10

i = 1

prod = 1

while i < 10:

    if i % 3 == 0:

      prod = prod * i

    i = i + 1

print(prod )        