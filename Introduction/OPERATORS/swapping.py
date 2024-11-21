#wap to swap two variables
# a="hello" b=10 then swap 

a = "hey" # cls str
b = "10" #cls int

print(f"a={a} ,b={b} before swapping")
temp = a
a = b
b = temp
print(f"a={a}, b={b} after swapping")

# taking an another variable called temp then swapping the values of a and b
#over writing 

#without using third variable

# a=10 b= hello
a,b = b,a  # overwrite this values of a and b 

# after overwriting
# a=hello b=10

a= "hi nanna"
b= "hi bony"


temp = a 
a = b
b = temp
print(a)
print(b)