

# write a function  for  the sum  of numbers using  decorator


def positive(fn):

    def wrapper(*args):  #(1,2,3,4)


        for i in args:

            if i < 0:       # this is the condition for negative values

                print("Enter positive value: ")

                break

        else:  # for positive values

            return fn(*args)

    return wrapper           


@positive


def sum(*args):

    sum = 0

    for i in args:

        sum += i
    print(sum)    

sum(5,6,2)