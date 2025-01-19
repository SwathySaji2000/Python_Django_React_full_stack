class Shape:

    def area(self,length,breadth):
        print(length * breadth)

    def perimeter(self,length,breadth):

        if length == breadth:

            print(4 * length)

        else:

            print(2*(length + breadth))

class Rectangle(Shape):

    pass

class Square(Shape):

    pass


length = int(input("Enter the length: "))

breadth = int(input("Enter the breadth: "))


obj = Rectangle()

obj.perimeter(length = length,breadth=breadth)

obj.area(length = length,breadth=breadth)

obj = Square()

obj.perimeter(length = length,breadth=breadth)

obj.area(length = length,breadth=breadth)

