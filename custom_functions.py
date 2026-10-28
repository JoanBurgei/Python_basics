# from unittest import answer
from hashlib import file_digest


def greet():
    print("Hello")

def greeting(name):
    print(f"Hello, {name}")

def volume_cylinder(radius,height):
    v= 22/7 * radius**2 * height
    print(round(v,2))

    # function that saves your answer in a file
def volume_cylinder_better(radius,height):
    v= 22/7 * radius**2 * height
#it should not print instead it will return
    return v

def volume_surface(radius,height):
    v = 22/7 * radius**2 * height
    a = 22/7 * radius**2 * 2 + 22/7 *radius *2 * height
    return v,a


greet()# calling function == use it / no arguments/parameters

greeting("sila")
greeting("ahmed")
greeting("juliet")

volume_cylinder(14,20)
volume_cylinder(4,12)

result = volume_cylinder_better(6.5, 8.5)
print(round(result,3))

with open("volume.txt", "w") as file:
    file.write(str(result))

volume, area = volume_surface(10,20)
print(f"volume is {round(volume,2)}, area is {round(area,2)}")

# named parameters
v,a = volume_surface(radius = 10,height = 10)
print(f"volume  is {round(v,2)} and area is {round(a,2)}")

def divide(a=1,b=1, should_round= False):
    res =  a / b
    if should_round == True:
        return round(res,2)
    else:
        return res
print(divide(9.1,5.11 , True))
print(divide(b = 7 , should_round= True))
