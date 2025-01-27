
# Method overriding  # same method in different classess 

# without inheritance we cant do polymorphisim

#  allows a derived class to provide a specific implementation of a method  i.e already defined in ts base class.

# method extension case we are normally using this polymorphisim..


class A:

    def method1(self):

        print("i am super class")

class B(A):

    def method1(self):
       print("I am base class") 


obj = B()
obj.method1()

obj2 = A()
obj2.method1()