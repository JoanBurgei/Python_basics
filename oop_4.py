#Inheritance
from oop import p1
from oop_2 import c1


class employee:
    def __init__(self, name, email, department, salary):
        self.name = name
        self.email = email
        self.department = department
        self.salary = salary

    def show_details(self):
        print(self.name, self.email ,self.department, self.salary)


class PermanentEmployee(employee):
    def __init__(self, name, email, increment, department, salary, cover):
        super().__init__(name, email, department, salary)  #calls parent class
        self.cover = cover
        self.increment = increment


class ContractEmployee(employee):
    def __init__(self, name, email, department, salary, tenure):
        super().__init__(name, email, department, salary)
        self.tenure = tenure


p1 = PermanentEmployee("Joy Mumo", "jm@gmail.com", 2, "HR", 68000, "Britam")
c1 = ContractEmployee("Adam Mohammed", "am@gmail.com", "IT", "25000", 2000)

p1.show_details()

c1.show_details()
#TODO overriding
#oop in python tutorial
# classes in python tutorial