#### Decorators  { for rexample i need to visit cart ina website ,, i should login to the website  so we can use decorator}

#  higher functions that modify behaivour of functions without altering their original code ...


# we can't use decorator method in class


#  "decorator" is a higher order function which takes a function as a parameter.

def decorator(fn):  # which is a higher order function decorator uses another function { def wrapper}

    def wrapper():

        print("Welcome")

        return fn
    
    return wrapper()

@decorator         

def greet():   

    print("Hello")

greet()











def swap_numbers(func):   # always  func mattoru function - ne call 

    def wrapper(a,b):

        if b == 0:

            a,b = b,a

        return func(a,b)
    return wrapper
    

@swap_numbers
def division(a,b):   # without any modification of body 

    print(a/b)

division(0,5)    


    