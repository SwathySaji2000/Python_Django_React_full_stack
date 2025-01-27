
#  Abstract Method: method without body is known as abstract class 

# Abstract class: class that contain abstract method is known as abstract class

# python does not support abstract class so it is a partially object oriented programming language..


class A: # abstract class

    def abc(self):
        pass

from abc import ABC, abstractmethod

class Vehicle(ABC):

    def start_engine(self):
        print("start engine")

    def stop_engine(self):
        print("engine stopped")

    @abstractmethod # decorator

    def change_gear(self):
        pass


class Car(Vehicle):

    def change_gear(self):
        print("change gear")


obj = Car()
obj.change_gear()           
            


         

