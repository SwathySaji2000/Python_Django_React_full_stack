# crete a class called Mark

# method1: add marks of 5 subjects of a student and add it to a list

# method2: display the average of  marks 

class Mark:

    def __init__(self,name):

        self.name = name 
        self.data = []
        self.details  = {}

    def add_marks(self,*args):  # tuple

        # self.marks = marks
        # self.data.append(marks)   
        # print(self.data) 

        for  i in args:   # by using we can pass number of arguments to a function
            self.data.append(i)   # args can be used without calling the method repeatedly 
        print(self.data)    
          

    def avg(self):
        
        sum = 0

        for i in self.data:

            sum += i
            avg = sum/len(self.data)
            

        print(f"your average marks is {avg}")

        self.details [self.name] =  self.avg

    def details(self):
        print(f"{self.details}")    

    
    def __str__(self):  # returns a human readable , informal ,string representation of an object
        return self.name         


obj = Mark(name = "swathy")  # by using init function we can directly pass the arguments

obj.add_marks(90,70,40,50,60)


obj.avg()

