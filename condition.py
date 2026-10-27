# if else
import os

from numbers import age
name = input("What is your name? ")
age = input("Enter your age: ")
if not age.isnumeric():
    print("Invalid age")
    # teminate
    os._exit(0)
    #sys.exit(0)

# age = int(input("Enter your age: "))
# age = int(age)

if int(age) > 18:
    print(name + " is an Adult")
else:
    print(name + " is a Child.")

#lists, boolean, tuples,dictionary, loops

