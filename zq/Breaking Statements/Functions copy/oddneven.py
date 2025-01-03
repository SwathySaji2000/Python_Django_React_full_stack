# wap to find the sum of odd n even numbers
# using function

def number(*args):
    even_sum = 0
    odd_sum = 0
    
    # Iterate through the numbers

    for i in args:
        if i % 2 != 0:
            odd_sum += i
        else:
            even_sum += i

   
    print(f"Sum of even numbers: {even_sum}")
    
    print(f"Sum of odd numbers: {odd_sum}")

# Function calls
number(6, 8, 1)
number(3, 9, 12)



