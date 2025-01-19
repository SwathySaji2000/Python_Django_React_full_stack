
class Abc:

    def __init__(self,name,salary):

        self.name = name

        self.salary = salary


    def display(self):

        print(f"Name: {self.name}")  
        print(f"Salary: {self.salary}")


class Def(Abc):

    def __init__(self, name, salary,department):
        super().__init__(name, salary)

        self.department = department


    def display(self):
        super().display()

        print(f"Department: {self.department}")


obj=Def(name="henna",salary="12000",department="Trainer")   
obj.display()  




    

      
        
          


        