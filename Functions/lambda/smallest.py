 # wap to find the smallest number using lambda

n = lambda a,b,c : a if (a<b and a<c) else b if (b<a and b<c) else c

print(n(9,3,4))

