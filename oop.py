#oop
#object --> laptop ->
# name --> props
# classes

class Person:
    # constructor
    def __init__(self, name, dob, color, weight, height):
        self.name = name
        self.dob = dob
        self.color = color
        self.weight = weight
        self.height = height
    def display(self):
        print(f"Name is {self.name} and DOB is {self.dob}")

    def get_bmi(self):
        result = self.weight/ self.height**2
        return round(result,2)


# blueprint for creating objects

p1 = Person("Hun Chink", "08-09-2001", "Black", 65.88, 1.85)
p2 = Person("Maria Asha", "31-12-2005", "White", 60.0, 1.72)

p1.display()
p2.display()

print(f"{p1.name} bmi is {p1.get_bmi()}") # Ctrl + D
print(f"{p2.name} bmi is {p2.get_bmi()}") # Ctrl + D