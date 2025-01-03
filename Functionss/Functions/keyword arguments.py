
### keyword arguments


# send arguments with the key = value syntax. this way the order of the arguments does not matter.

def detail(name,course,place):

    print(f"ur name is {name}, ur course is {course}, you are from {place}")

detail(course="django", place ="kottayam",name="swathy")


##### Default arguments

# python  allows function arguments have default values. if the function without arguments, the argument get its default value.
# it only allows in the last.


def detail(name,place,gender = None):

    print(f"ur name is {name}, ur  from {place}, your gender is {gender}")

detail(name= "swathy", place ="kottayam",gender="female")