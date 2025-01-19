#create a class and display in a dictonary {'anna': {'age': 23, 'mark': 67}}  

# name, {}

# add mark,age'

# get mark,age

# upadate mark


class Student:

    def __init__(self,name):
        self.name = name
        self.data ={}

    def add_marks(self,age,mark):
        self.age = age
        self.mark = mark
        self.data[self.name] = {"age": age,"mark":mark}  # we call dict[which include name as key: {value}]  nested dict
        print(self.data)

    def get_marks(self):
        return self.data[self.name].get('mark')   

    def get_age(self):
        return self.data[self.name].get('age')  # .get is used to get the value of age , if keyword doesn't match it returns """None"""
    

    # def update_mark(self,mark):

    #     self.data[self.name]['mark'] = mark
    #     return self.data
    
    def update(self,mark=None,age=None):    

        if age == None:
            self.data[self.name]['mark']=mark
            return self.data
        
        elif mark == None:
            self.data[self.name]['age']=age
            return self.data

        else:
            self.data[self.name]['mark']=mark   
            self.data[self.name]['age']=age
            return self.data

obj=Student(name="anna")

obj.add_marks(age=23,mark=67)

print(obj.get_marks())
print(obj.get_age())
print(obj.update())
print(obj.update())
    