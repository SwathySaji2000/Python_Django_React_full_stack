# wap to find the largest amoung 3 numbers

largest = lambda a,b,c: a if (a>b and a>c) else  b if (b>a and b>c) else c  # if inte akath if without using elif 

print(largest(8,4,6))