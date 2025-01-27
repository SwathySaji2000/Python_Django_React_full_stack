
# wap that implements a decorator to enforce type checking on the arguments of a function.

def type_check(fn):

    def wrapper(*args):

        for i in args:

            print(type(i),i)  # finding the type and display i in console

        return fn(*args)
    return wrapper    

@type_check

def abc(*args):

    print("values entered successfully")

abc(1,"Hai",True)





