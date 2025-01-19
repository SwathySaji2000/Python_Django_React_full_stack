#wap student details


class Student:

    def __init__(self,name,age,marks):   # i.e constructor : is a special method that is called automatically when an object is creted from a class

        self.name = name
        self.age = age
        self.marks = marks

    def method1(self):

        print(f"hey {self.name} and you have {self.marks} ")
    
    def method2(self):
        print(f"hey {self.name} , your age is {self.age} and you have {self.marks}")

student1 = Student(name="neenu",age=20,marks=56) 
student2 = Student(name = "meenu",age = 29, marks =22)
student2.method1()
student2.method2()
student1.method1()
student1.method2()

            