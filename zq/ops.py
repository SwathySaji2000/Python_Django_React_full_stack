## inheritance

# class Parent:

#     def car(self,name):

#         self.name = name

#     def display(self):

#         print(self.name)

# class Child(Parent):
#     pass

# obj = Parent()
# obj.car(name="audi")
# obj.display()

# obj = Child()

# obj.display()



# class Abc:

#     def __init__(self,name,salary):

#         self.name = name
#         self.salary = salary

#     def display(self):

#         print(f"name : {self.name}")

#         print(f"salary: {self.salary}")    


# class Def(Abc):

#     def __init__(self, name, salary,department):
#         super().__init__(name, salary)

#         self.department = department


#     def display(self):
#         super().display()  

#         print(f"department:{self.department}")


# obj = Def(name="Dia",salary=5600,department="Trainee")
# obj.display()


class Shape:

    def area(self,length,breadth):

        self.length = length
        self.breadth = breadth

        print(f"Area of a Rectangle = {length * breadth}")

        print(f"Area of a square : (2 ** {length})")


    

    def perimeter(self,length,breadth):

        if self.length == self.breadth:

            print(f"Perimeter of a square = 4 *{length}")

          
        else:
             
            print(f"Perimeter of a rectangle: {(2*(length + breadth))}")



class Rectangle(Shape):
    pass

class Square(Shape):
    pass
length = int(input("Enter the length: "))

breadth = int(input("Enter the breadth: "))

obj = Rectangle()

obj.area(length=length,breadth=breadth) 

obj.perimeter(length=length,breadth=breadth)

obj = Square()

obj.area(length=length,breadth=breadth)

obj.perimeter(length=length,breadth=breadth)


        
   

        

   
                
        













