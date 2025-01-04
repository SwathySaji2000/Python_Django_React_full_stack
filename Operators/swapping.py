#wap to swap two variables
# a="hello" b=10 then swap 

a = "hey" # cls str
b = "10"
#c = "45" #cls int

print(f"a={a} ,b={b} before swapping")
temp = a
a = b
b = temp
#c = temp
print(f"a={a}, b={b} after swapping")

# taking an another variable called temp then swapping the values of a and b
#over writing 

#without using third variable

# a=10 b= hello
a,b = b,a  # overwrite this values of a and b 

# after overwriting
# a=hello b=10



