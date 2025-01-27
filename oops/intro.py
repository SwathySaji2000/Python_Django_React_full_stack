#############  OOPS
 

# python is object oriented programming language.  [partially because abstract class does not support ]

# class is a  blue print of object to be  created.
# Objects can also contain methods. 
# Methods in objects are functions that belong to the object.

# in every class in the function , we need to declare (self) is used to access variables that belong to the class


class Student:

    def details(self,name,place):  # details and show_details are methods ,, self is used to calling the parameters repeatedly 

        self.name = name
        self.place = place

        print(f" welcome {name}")

    def show_details(self):

        print(f"Welcome {self.name}, from {self.place}")    


    def __str__(self):  # returns a human readable , informal ,string representation of an object
        return self.name     

obj1 = Student()  
obj1.details(name="swathy",place="kottayam")  
obj1.show_details() 

