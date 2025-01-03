

# wap to find the number[count]  of arguments in type(int) using a function
# with *args

#function("abc,1,True,false,0,7.8,5")

# if type(num) == int


def count_type(*args):

    count = 0

    for i in args:
   

        if type(i) == int:

            count += 1

    print(f" The number of arguments in type of int is {count}")

count_type("abc",1,"True","False",0,7.8,5)   